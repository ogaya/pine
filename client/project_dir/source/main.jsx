var Hello = require('./components/hello2-af');
var React = require('react');
var Header = require('./components/header/uf-header');
var Menu = require('./components/menu/side-menu');
var Tab = require('./components/tab/tab');

React.render(
    <Header />,
    document.getElementById('header')
);

React.render(
    <Menu />,
    document.getElementById('menu')
);

React.render(
    <Tab />,
    document.getElementById('tab')
);
