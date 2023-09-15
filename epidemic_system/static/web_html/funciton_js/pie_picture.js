function pie_option_fun(ECharts){
    ECharts.showLoading()
    var optionPie = {
        animation:true, //配置动画是否开启
        animationDuration:5000, //配置动画时长，单位毫秒
        title:{
            text: "国外现有确诊数据分布",
            font_family: "楷体",
            left: 10,
            top: 0,
            textStyle:{
                color: '#FF1493',
                fontSize : '18',
                fontFamily: "楷体",
                color: 'white'
            }
        },
        tooltip: {
                trigger: 'item',   //触发类型，item:数据项图形触发
        },
        legend:{
            orient: 'vertical',
            top: 10,
            left: 'right',
            textStyle: {
                fontSize: 18,
                fontFamily: "楷体"
            }
        },
        series:[
            {
                name: '国外现有确诊数据分布',
                type: 'pie',
                radius: ['35%', '60%'], //第0个元素代表的是内圆的半径，第1个元素外圆的半径
                avoidLabelOverlap: false,
                label: {
                    show: false, // 设置十否显示标签标题
                    position: 'center' //默认在外边
                },
                emphasis: {
                    label: {
                        show: true,
                        fontSize: '15',
                        fontWeight: 'bold'
                    }
                },
                    labelLine: {
                    show: true
                },
                data: [],
                color:[],
                // selectedMode:'single', //选择的区域会脱离原点一小段距离
                selectedMode:'multiple', //可连续选择区域进行脱离效果
                selectedOffset:20, //选择区域脱离的偏移量
            }
        ]
    };
    ECharts.hideLoading()
    return optionPie
}

var pie_echarts = echarts.init(document.querySelector("#pie"), "dark")
var pie_option = pie_option_fun(pie_echarts)
pie_echarts.setOption(pie_option)
