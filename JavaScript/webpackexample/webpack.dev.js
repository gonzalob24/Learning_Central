const path = require("path");
const common = require("./webpack.common");
const {merge} = require("webpack-merge");

// merge common and my object in webpack dev
module.exports = merge(common, {
    mode: "development",
    output: {
        filename: "[name].bundle.js", // bust caching
        path: path.resolve(__dirname, "dist")
    }
});