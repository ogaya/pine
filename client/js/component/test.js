var t = require("test2");
var data = [
    {author: "Pete Hunt", text: "This is one comment"},
    {author: "Jordan Walke", text: "This is *another* comment"}
];

var Counter = React.createClass({
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
            <div>
            <span>{this.state.count}</span>
            <button onClick={this.onClick}>click</button>
            </div>
        );
    }
});

var Commenter = React.createClass({
    render: function() {
        return (
            <div className="comment">
            <h2 className="commentAuthor">
            {this.props.data}
            </h2>
            </div>
        );
    }
});

var CommentList = React.createClass({
    render: function() {
        return (
            <div className="commentList">
            Hello, world! I am a CommentList.
            </div>
        );
    }
});

var CommentForm = React.createClass({
    render: function() {
        return (
            <div className="commentForm">
            Hello, world! I am a CommentForm.
            </div>
        );
    }
});


var CommentBox = React.createClass({
    render: function() {
        return (

            <div className="commentBox">
            <h1>Comments</h1>
            <CommentList />
            <Commenter data={this.props.name} />
            <CommentForm />
            <Counter />
            </div>
        );
    }
});
React.render(
    <CommentBox name="abcd" />,
    document.getElementById('content')
);
