const path = require("path");
const common = require("./webpack.common");
const {merge} = require("webpack-merge");
const { CleanWebpackPlugin } = require("clean-webpack-plugin");

module.exports = merge(common, {
    mode: "production",
    output: {
        filename: "[name].[contentHash].bundle.js", // bust caching, factor main --> [name] because it will be main or
                                            // vendor
        path: path.resolve(__dirname, "dist")
    },
    plugins: [new CleanWebpackPlugin()]
});