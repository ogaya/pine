var _select_tag = "2AI001";
var _select_tab = "olsTab";

// 上下限値を切り捨て
function convert_limit_text(val, scale){
    //var minus = (val < 0);
    var abs = Math.abs(val);

    if (abs > Math.pow(10, scale)) return "large";
    if (abs < Math.pow(10, -scale)) return "mini";
    return val.toFixed(scale);
}

function set_content_detail(li){

    li.selectAll("a").remove();
    // リストアイテムの基盤
    var root = li.append("a").append("div").attr("class",function(d){
        var commonClass = "content_detail";
        if (d.r_squared >= 0.90) return commonClass + " best_result";
        if (d.r_squared >= 0.40) return commonClass + " good_result";
        return commonClass + " bad_result";
    });

    // 統計値
    var fdiv = root.append("div").text(function(d) {
        var t = new Date(d.obj_time);
        var time_txt = "【データ時間：" + t.getFullYear() + "/" + (t.getMonth() + 1)+ "/"+ t.getDate() + "】";
        return "決定係数：" + d.r_squared.toFixed(2) + " " + time_txt;
    });

    var expdiv = root.append("div").attr("style","display=inline").selectAll("div")
    .data(function(d){
        var items = [];
        d.t.forEach(function(v,i){
            var item = {};
            item.t = v;
            item.coef = d.coefficient[i];
            item.exptext = (i == 0) ? "切片" : d.explanatory[i - 1];
            items.push(item);
        });
        items.sort(function(x,y){
            var x_abs = Math.abs(x.t);
            var y_abs = Math.abs(y.t);

            if (x_abs < y_abs) return 1;
            if (x_abs > y_abs) return -1;
            return 0;

        });
        return items;
    }).enter().append("div");

    expdiv.
    attr("class",function(d){
        var t_abs = Math.abs(d.t);
        var coef_abs = Math.abs(d.coef);
        if (t_abs < 2 ) 
            return "simple_info worst_t";
        if (coef_abs < 0.001)
            return "simple_info worst_t";
        if (t_abs < 100)
            return "simple_info bad_t";
        return "simple_info good_t"; 
    })
    .text(function(d) {
        return d.exptext + "（"   + convert_limit_text(d.coef, 3) +  "）";
    });
}

function set_content_corr(li){
    li.selectAll("a").remove();
    // リストアイテムの基盤
    var root = li.append("a").append("div").attr("class",function(d){
        var commonClass = "content_corr";
        var val = Math.abs(d.val);
        if (val >= 0.70) return commonClass + " best_result";
        if (val >= 0.40) return commonClass + " good_result";
        return commonClass + " bad_result";
    });
    //.text(function(d) {
        //    return d.y + "（" + convert_limit_text(d.val, 3) + "）" + "【データ時間：" + d.y_time + "】";
    //});

    root.append("div")
    .attr("class", "content_corr_detail")
    .text(function(d){
        return d.y;
    });

    root.append("div")
    .attr("class", "content_corr_detail")
    .text(function(d){
        return "（" + convert_limit_text(d.val, 3) + "）";
    });

    root.append("div")
    .attr("class", "content_corr_detail")
    .text(function(d){
        var t = new Date(d.y_time);
        return "【データ時間：" + t.getFullYear() + "/" + (t.getMonth() + 1)+ "/"+ t.getDate() + "】";
    });

}

function reload_content_ols(tag){
    var url = "/htbin/statistics_result.py?objective=" + tag;
    d3.json(url,function(error,dat){
        if (error != null){
            console.log(error);
            d3.select("#content_ul").selectAll("li").remove();
            return;
        }

        var li = d3.select("#content_ul").selectAll("li").data(dat);

        li.enter().append("li");
        li.exit().remove();
        set_content_detail(li);

    });
}

function reload_content_corr(tag){
    var url = "/htbin/correlation.py?x=" + tag;
    d3.json(url,function(error,dat){
        if (error != null){
            console.log(error);
            d3.select("#content_ul").selectAll("li").remove();
            return;
        }

        dat.sort(function(x,y){
            var x_abs = Math.abs(x.val);
            var y_abs = Math.abs(y.val);

            if (x_abs < y_abs) return 1;
            if (y_abs > y_abs) return -1;
            return 0;

        });

        var li = d3.select("#content_ul").selectAll("li").data(dat);

        li.enter().append("li");
        li.exit().remove();
        set_content_corr(li);
    });
}

function reload_content(tag, tab){
    if (tab == "olsTab"){
        reload_content_ols(tag);
        return;
    }
    if (tab == "corrTab"){

        reload_content_corr(tag);
        return;
    }
    d3.select("#content_ul").selectAll("li").remove();
}
function sideItemClick(tag,tab){
    _select_tag = tag;
    d3.select("#tagTab").text(tag);
    reload_content(tag, _select_tab);
}

function contentTabClick(tab){
    _select_tab = tab;
    d3.select("#contentMenu").selectAll("a")
    .attr("class","contentMenuNonSelect");

    d3.select("#" + tab).attr("class","contentMenuSelect");

    reload_content(_select_tag, tab);
}

function reload_sidemenu(){
    d3.json("/htbin/target.py",function(error,data){

        if (error != null){
            console.log(error);
            return;
        }

        d3.select("#sideList")
        .selectAll("li")
        .data(data)
        .enter()
        .append("li")
        .append("a")
        .text(function(d) {return d.tag;})
        .attr("href", function(d) {return "javascript:sideItemClick('"+ d.tag + "')";});
    });
}

// ウィンドウ表示時の処理
window.onload = function(){
    reload_sidemenu();
    d3.select("#content").append("ul").attr("id","content_ul");
    sideItemClick("2AI001");
};
