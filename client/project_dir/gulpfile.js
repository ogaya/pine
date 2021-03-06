var gulp = require('gulp');
var webpack = require('gulp-webpack');
var webpackConfig = require('./webpack.config.js');
var requireDir = require('require-dir');

gulp.task('cleanBuild', function (cb) {
    var rimraf = require('rimraf');
    rimraf('./build/', cb);
});

gulp.task('copyIndex', ['cleanBuild'], function () {
    return gulp.src('./source/index.html')
    .pipe(gulp.dest('./build/'));
});

gulp.task('build', ['copyIndex'], function (cb) {
    return gulp.src('')
    .pipe(webpack(webpackConfig))
    .pipe(gulp.dest(''));
});

gulp.task('watch', function() {
    gulp.watch('./source/**/**/*.*',['build']);
});
