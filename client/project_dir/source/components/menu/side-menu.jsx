var React = require('react');
var request = require('superagent');

var style = {
    container:{
        zIndex:"10",
        backgroundColor:"#F9F9F9",
        display:"inline-block",
        position:"absolute",
        width:"200px",
        boxShadow: "0 0 5px rgba(0,0,0,1)",
        right:"0px",
        top:"50px",
        margin:"10px",
        height:"300px",
        border:"1px solid #123"
    },
    title:{
        fontSize:"15px",
        padding:"5px 10px",
        color:"#FFF",
        backgroundColor:"#212E4D"
    }
}

var Menu = React.createClass({
    getInitialState: function () {
        return { name: "not clicked" ,targets:[] };
    },
    componentDidMount: function(){
        request.get('/htbin/target.py', res => {
            this.setState({targets:res.body});
        });
    },
    onClick: function () {
        this.setState( {name: "clicked" });
    },
    render: function() {
        var list = this.state.targets.map((target) =>{
            return (
                <div>{target.tag}</div>
            );

        });
        return (
            <div style={style.container}>
                <div style={style.title}>ターゲット</div>
                {list}
            </div>
        );
    }
});

module.exports = Menu;
