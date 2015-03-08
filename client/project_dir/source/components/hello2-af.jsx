var React = require('react');
var Helloo = React.createClass({
    getInitialState: function () {
        return { name: "not clicked"  };
    },
    onClick: function () {
        this.setState( {name: "clicked" });
    },
    render: function() {
        return (
            <div onClick={ this.onClick } >
                <div>{this.state.name}</div>
                <div>te</div> 
            </div>
        );
    }
});

module.exports = Helloo;
