"use strict";
var gulp = require('gulp');
var browserSync = require('browser-sync').create();
var exec = require('child_process').exec;
var jsDir = 'static/js/';
var cssDir = 'static/css/';
var templateDir = 'templates/';

gulp.task('runserver', function () {
    /*var proc = exec('"C:\\Users\\Kevin Mike\\citationsEnv\\Scripts\\activate"; PYTHONUNBUFFERED=1 ./manage.py runserver');*/
    var proc = exec('"C:\\Users\\Kevin Mike\\citationsEnv\\Scripts\\activate"; python -u ./manage.py runserver');
    proc.stderr.on('data', function (data) {
        process.stdout.write(data)
    });
    proc.stdout.on('data', function (data) {
        process.stdout.write(data)
    });
});

gulp.task('browser-sync', function () {
    browserSync.init({
        proxy: 'http://localhost:8000',
        port: 80
    });
});

gulp.task('js', function () {
    return gulp.src(jsDir + '*.js')
        .pipe(browserSync.reload({stream: true}));
});

gulp.task('css', function () {
    return gulp.src(cssDir + '*.css')
        .pipe(browserSync.reload({stream: true}));
});

gulp.task('default', ['runserver'], function () {
    //gulp.watch('*.html').on('change', browserSync.reload);
    gulp.watch(templateDir + '*.html', browserSync.reload);
    gulp.watch(cssDir + '*.css', ['css']);
    gulp.watch(jsDir + '*.js', ['js']);
});