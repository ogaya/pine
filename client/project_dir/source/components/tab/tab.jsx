var React = require('react');
var request = require('superagent');

var style = {
    container:{
        fontSize:"16px",
        position:"absolute",
        display:"inline",
        borderBottom:"1px solid #89A3BB",
        width:"calc(100% - 240px)",
        height:"32px",
        margin:"10px",
        padding:"0px 5px",
        top:"50px"
    },
    detail:{
        backgroundColor:"#212E4D",
        borderTop:"1px solid #557",
        borderLeft:"none",
        borderRight:"none",
        borderBottom:"1px solid #89A3BB",
        color:"#AAA",
        display:"inline-block",
        minWidth:"120px",
        margin:"0px",
        height:"27px",
        padding:"4px 5px 0px 5px",
        verticalAlign:"middle",
        textAlign:"center",
        textDecoration: "none"

    }
}

var Tab = React.createClass({
    getDefaultProps(){
        return {
            tagItems:[
                {key : "tag", text : "tag"},
                {key : "ols", text : "多変量解析"}

            ]

        };
    },
    render: function() {
        var list = this.props.tagItems.map((item) =>{
            return (
                <a style={style.detail}>{item.text}</a>
            );

        });
        return (
            <div style={style.container}>
                {list}
            </div>
        );
    }
});

module.exports = Tab;
