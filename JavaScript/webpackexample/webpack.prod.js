const path = require("path");
const common = require("./webpack.common");
const { merge } = require("webpack-merge");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const OptimizeCSSAssetsPlugin = require("optimize-css-assets-webpack-plugin");
const TerserPlugin = require("terser-webpack-plugin");
var HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = merge(common, {
  mode: "production",
  output: {
    filename: "[name].[contentHash].bundle.js", // bust caching, factor main --> [name] because it will be main or
    // vendor
    path: path.resolve(__dirname, "dist"),
  },
  optimization: {
    minimizer: [
      new OptimizeCSSAssetsPlugin(),
      new TerserPlugin(), // vendor.js file was no longer being minified add in plugin that was being used
      //turser webpack plugin, was being used by default.
      new HtmlWebpackPlugin({
        template: "./src/template.html",
        minify: {
          removeAttributeQuotes: true,
          collapseWhitespace: true,
          removeComments: true,
        },
      }),
    ],
  },
  plugins: [
    new MiniCssExtractPlugin({
      filename: "[name].[contentHash].css",
    }),
    new CleanWebpackPlugin(),
  ],
  module: {
    rules: [
      {
        test: /\.scss$/, // webpack needs to know about this so I imported main.css in index.js. I can just use .scss becuase scss is not valid css code. So, I have to use another loader. Use sass-loader --> turns code into valid css and then css and style loader will take care of the rest.
        use: [
          MiniCssExtractPlugin.loader, //3. Extract css into files
          "css-loader", // 2. Turns css into JS code
          "sass-loader", // 1. Turns sass into valid css
        ], // takes sass turn into valid css code, css-loader turns file into valid JS code and style injects code into the DOM
      },
    ],
  },
});
