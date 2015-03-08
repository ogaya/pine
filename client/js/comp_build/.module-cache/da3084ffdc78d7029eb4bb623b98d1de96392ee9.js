var data = [
    {author: "Pete Hunt", text: "This is one comment"},
    {author: "Jordan Walke", text: "This is *another* comment"}
];

var Counter = React.createClass({displayName: "Counter",
    getInitialState:function() {
        return {
            count: 0
        };
    },
    onClick:function() {
        this.setState({ count: this.state.count + 1});
    },
    render:function() {
        return (
            React.createElement("div", null, 
            React.createElement("span", null, this.state.count), 
            React.createElement("button", {onClick: this.onClick}, "click")
            )
        );
    }
});

var Commenter = React.createClass({displayName: "Commenter",
    render: function() {
        return (
            React.createElement("div", {className: "comment"}, 
            React.createElement("h2", {className: "commentAuthor"}, 
            this.props.data
            )
            )
        );
    }
});

var CommentList = React.createClass({displayName: "CommentList",
    render: function() {
        return (
            React.createElement("div", {className: "commentList"}, 
            "Hello, world! I am a CommentList."
            )
        );
    }
});

var CommentForm = React.createClass({displayName: "CommentForm",
    render: function() {
        return (
            React.createElement("div", {className: "commentForm"}, 
            "Hello, world! I am a CommentForm."
            )
        );
    }
});


var CommentBox = React.createClass({displayName: "CommentBox",
    render: function() {
        return (

            React.createElement("div", {className: "commentBox"}, 
            React.createElement("h1", null, "Comments"), 
            React.createElement(CommentList, null), 
            React.createElement(Commenter, {data: this.props.name}), 
            React.createElement(CommentForm, null), 
            React.createElement(Counter, null)
            )
        );
    }
});
React.render(
    React.createElement(CommentBox, {name: "abcd"}),
    document.getElementById('content')
);
