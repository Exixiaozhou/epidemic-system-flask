function map_option_fun(ECharts){
    ECharts.showLoading()
    var optionMap = {
        backgroundColor: '#333',
        title: {
            text:'',
            subtext: '',
            x: 'left',
            textStyle:{
                color: '#F8F8FF',
                fontSize : '18',
                fontFamily: "楷体",
            }
        },
        tooltip: {
            trigger : 'item'
        },
        series: [{
            name: '累计确诊人数',
            type: 'map',
            mapType: 'china',
            roam: false, //拖动和缩放
            label: {
                normal : {
                    show:true,
                    fontSize:12,
                    color: 'blue'
                },
                emphasis: {
                    show:true,
                    fontSize : 18, //点击后的颜色
                    fontFamily: "楷体", //点击后显示的字体
                    color: "red", //文字颜色
                },
            },
            itemStyle:{ //设置地图背景色
                 color: ""
            },
            emphasis: { //点击后的背景颜色
                itemStyle: {
                    areaColor: "#b4ffff"
                }
            },
            data: []
        }],
        //左侧小导航图标
        visualMap: {
            show : true,
            textStyle: {
                color: '#red',
                fontSize : '18',
                fontFamily: "楷体",
            },
            x: 'left',
            y: 'top', //bottom
            pieces: [
                {min: 0, max: 0, label: '0', color: '#fff'},
                {min: 1, max: 9, label: '1-9', color: '#ffe4da'},
                {min: 10, max: 99, label: '10-99', color: '#ff937f'},
                {min: 100, max: 999, label: '100-999', color: '#ff6c5e'},
                {min: 1000, max: 9999, label: '1000-9999', color: '#fe3335'},
                {min: 10000, label: '>=100000', color: '#cd0000'},
            ],
            itemWidthL: 10, // 显示的标签宽、高、行高设置
            itemHeight: 10,
            itemGap: 10,
            inverse: false
        },
    };
    ECharts.hideLoading()
    return optionMap
}

var map_echarts = echarts.init(document.querySelector('#map'));
var map_option = map_option_fun(map_echarts)
map_echarts.setOption(map_option);
