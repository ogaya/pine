var React = require('react');
var ufo = require('./UFO.png');

var style = {
    container:{
        padding:"0px 10px",
        position:"absolute",
        top:"0px",
        left:"0px",
        zIndex:"100",
        width:"calc(100% - 20px)",
        height:"38px",
        backgroundColor:"#212E4D",
        color:"#FFF",
        boxShadow: "0 0 5px rgba(0,0,0,1)",
        borderBottom:"1px solid #123",
        margin:"0px",
        lineHeight:"20px"
    },
    titleIcon:{
        margin:"6px 0px 4px 0px",
        width:"48px",
        height:"25px"
    },
    headerItem:{
        display:"inline-block",
        verticalAlign:"middle",
        fontWeight:"bold",
        margin:"0px 0px 0px 10px"
    }
 
}
var Header = React.createClass({
    render: function() {
        return (
            <div style={style.container}>
                <div style={style.headerItem}>
                    <img style={style.titleIcon} src={ufo} />
                </div>
                <div style={style.headerItem}>Unknown Flight</div>
            </div>
        );
    }
});
module.exports = Header;
