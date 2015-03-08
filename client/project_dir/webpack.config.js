module.exports = {
    entry: './source/main.jsx',
    output: {
        filename: './build/[name].bundle.js'
    },
    devtool: 'inline-source-map',
    module: {
        loaders: [
            { test: /\.jsx$/, loader: 'babel-loader' },
            { test: /\.js$/, loader: 'babel-loader' },
            { test: /\.png$/, loader: 'url?limit=8192' }
        ]
    },
    resolve: {
        extensions: ['', '.js', '.jsx']
    }
};
