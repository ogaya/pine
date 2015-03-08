var Hello = require('./components/hello2-af');
var Button  = require('./components/uf-button');
var React = require('react');
var Header = require('./components/header/uf-header');
var Menu = require('./components/menu/side-menu');
React.render(
    <Button />,
    document.getElementById('example')
);

React.render(
    <Header />,
    document.getElementById('header')
);

React.render(
    <Menu />,
    document.getElementById('menu')
);
