const path = require('path');

module.exports = {
  outputDir: path.resolve(__dirname, '../frontend/dist'),
  publicPath: '/static/',
  assetsDir: 'static',
  configureWebpack: {
    output: {
      filename: 'js/[name].[contenthash].js',
      chunkFilename: 'js/[name].[contenthash].js',
    },
  },
  chainWebpack: config => {
    config.plugin('html').tap(args => {
      args[0].publicPath = '/static/';
      return args;
    });
  },
};