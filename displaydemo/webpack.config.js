const path = require('path')
const webpack = require('webpack')
const HTMLPlugin = require('html-webpack-plugin')  //这个插件需要依赖 webpack 插件
// const ExtractTextPlugin = require('extract-text-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const VueLoaderPlugin=require('vue-loader/lib/plugin')

const isDev = process.env.NODE_ENV === 'development' //我们在package.json中设置的环境变量，全部是存放在process.env中的


const config = {
    // model:'development',
    // devServer:{

    // },
    target:'web',
    entry: path.join(__dirname, 'src/index.js'),
    output: {
        filename: 'bundle.js',
        path: path.join(__dirname, 'dist')
    },

    resolve: {
        /*
         * 别名配置，配置之后，可以在别的js文件中直接使用require('d3')，将导入的文件作为一个模块导入到你需要的项目中，不用配置别也可会当作模块导入项目中，只是你要重复写路径而已。
         * */
        alias: {
            moment$: 'moment/moment.js'
        }
    },
    module: {
        rules: [
            //加载 vue 文件
            {
                // test的意思是：检测文件类型
                test: /\.vue$/,  //通过`vue-loader`工具，让 webpack 支持 .vue 文件的编译
                loader: 'vue-loader'
            },
            //加载 jsx 文件
            {
                test: /\.jsx$/,
                loader: 'babel-loader'
            },
            //加载 css 文件
            //webpack4.0+不能再使用ExtractTextPlugin
            // {
            //     test: /\.css$/,
            //     // use: [
            //     //     'style-loader',    //将css文件写到html代码里
            //     //     'css-loader'       //css 的loader
            //     // ]
            //     loader: ExtractTextPlugin.extract('style-loader', 'css-loader')
            // },

            //使用babel
            {
                test:/\.js$/,
                use:['babel-loader'],
                //不对这个进行babel转换，这里边已经打包好
                exclude:path.resolve(__dirname,'node_modules'),
                include:path.resolve(__dirname,'src'),
            },

            //加载css
            {
                test: /\.css$/,
                use: [
                  MiniCssExtractPlugin.loader,
                  "css-loader"
                ]
              },
            //加载图片
            {
                test: /\.(gif|jpg|jpeg|png|svg)$/,
                use: [
                    {
                        loader: 'url-loader',
                        options: {  //通过 optons 参数配置上面这个 url-loader 
                            limit: 1024, //如果图片的小于1024，则将图片转成 base64的代码，直接写到代码里去，减少http请求
                            // name: '[name]-smyh.[ext]',  //设置图片的文件名。smyh表示所有文件名中都带有这个字符，[ext]指的是文件格式
                            name: '[name].[ext]',
                            publicPath: "../images/",
                            outputPath: "images/"
                        }
                    }
                ]
            },

            //boostrap相关
            {
                test: /\.(eot|woff|woff2|svg|ttf)([\?]?.*)$/,
                loader: "file-loader"
            }

            // {
            //     test: /\.(woff|woff2)(\?v=\d+\.\d+\.\d+)?$/,
            //     loader: 'url?limit=10000&mimetype=application/font-woff'
            // }, {
            //     test: /\.ttf(\?v=\d+\.\d+\.\d+)?$/,
            //     loader: 'url?limit=10000&mimetype=application/octet-stream'
            // }, {
            //     test: /\.eot(\?v=\d+\.\d+\.\d+)?$/,
            //     loader: 'file'
            // }, {
            //     test: /\.svg(\?v=\d+\.\d+\.\d+)?$/,
            //     loader: "url?limit=10000&mimetype=image/svg+xml"
            // },
        ],

    },
    plugins: [
        new webpack.DefinePlugin({
            //下面这个插件很有用：在这里定义之后，我们就可以在项目的js代码中，直接调用 `process.evn.NODE_ENV` 来判断环境
            //比如说，开发环境中，会打印很多错误信息，但是这些内容并不需要放在生产环境中，这时就可以用到环境的判断
            'process.evn': {
                // NODE_ENV:'development'
                // NODE_ENV: isDev ? '"development"' : '"production"'
                NODE_ENV:JSON.stringify('development')
            }
        }),
        new HTMLPlugin(),
        new webpack.HotModuleReplacementPlugin(),
        new webpack.ProvidePlugin({
            "$": "jquery",
            "jQuery": "jquery",
            "window.jQuery": "jquery"
        }),
        new VueLoaderPlugin(),
        // new ExtractTextPlugin('styles.css'),
        new MiniCssExtractPlugin({
            // Options similar to the same options in webpackOptions.output
            // both options are optional
            filename: "[name].css",
            chunkFilename: "[id].css"
          }),
          new webpack.LoaderOptionsPlugin({
            options: {
                postcss: function() {
                    return [require('autoprefixer')];
                }
            }
        }),
    ]
}

config.devServer = {
    port: 8011,
    host: '0.0.0.0',  //注意，ip地址是字符串
    overlay: { // 如果有任何的错误，就让它显示到网页上
        errors: true
    },
    //open:true,
    hot: true
}
config.devtool = '#cheap-module-eval-source-map'
// config.devtool = 'source-map'
module.exports = config
// Vue.config.devtool=true