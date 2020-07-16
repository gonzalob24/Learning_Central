const path = require("path");
const common = require("./webpack.common");
var HtmlWebpackPlugin = require("html-webpack-plugin");
const { merge } = require("webpack-merge");

// merge common and my object in webpack dev
module.exports = merge(common, {
  mode: "development",
  output: {
    filename: "[name].bundle.js", // bust caching
    path: path.resolve(__dirname, "dist"),
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: "./src/template.html",
    }),
  ],
  module: {
    rules: [
      {
        test: /\.scss$/, // webpack needs to know about this so I imported main.css in index.js. I can just use .scss becuase scss is not valid css code. So, I have to use another loader. Use sass-loader --> turns code into valid css and then css and style loader will take care of the rest.
        use: [
          "style-loader", //3. Inject styles into DOM
          "css-loader", // 2. Turns css into JS code
          "sass-loader", // 1. Turns sass into valid css
        ], // takes sass turn into valid css code, css-loader turns file into valid JS code and style injects code into the DOM
      },
    ],
  },
});
