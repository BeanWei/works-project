/**
 * 展示单条曲线的公共方法
 * data: Y轴数据
 * idStr: HTML中定义的echartdiv的id
 * title: 图标的标题
 * Xdata: X轴的数据
 */
function showSingle(data, idStr, title, Xdata) {
    var myChart = echarts.init(document.getElementById(idStr));
    myChart.setOption(option = {
        //标题
        title: {
            text: title,
            subtext: 'NU7'
        },
        tooltip: {
            trigger: 'axis'
        },
        //图例名
        legend: {
            type:'scroll',
            //show: true,
            orient: 'vertical',//'horizontal', // 'vertical'
            x: 'right',
            y: 'top',
            selectedMode: 'single',
            //selected: selected,
            //width: 50,
            //align: 'auto',
            align: 'left',
            borderWidth: 4,
            padding: 10,    // [5, 10, 15, 20]
            marginleft: 10,
            itemGap: 20,
            data: data.map(function (item) {
                return item.name;
            })
        },
        grid: {
            top: '10%',
            left: '0%',   //图表距边框的距离
            right: '30%',
            bottom: '10%',
            containLabel: true
        },
        //工具框，可以选择
        toolbox: {
            x:'center',
            itemGap: 20,
            feature: {
                dataZoom: {},
                dataView: {readOnly: false},
                restore: {},
                saveAsImage: {},
            }
        },
        //x轴信息样式
        xAxis: {
            type: 'category',
            boundaryGap: false,
            data: Xdata,
            //坐标轴颜色
            // axisLine:{
            //     lineStyle:{
            //         color:'red'
            //     }
            // },
            //x轴文字旋转
            axisLabel:{
                rotate:30,
                interval:0
            },
        },

        yAxis : [
            {
                type : 'value',
                axisLabel : {
                    formatter: '{value}'
                }
            }
        ],
        series: data.map(function(item){
            return {
                name: item.name,
                type: item.type,
                symbol: item.symbol,
                symbolSize: item.symbolSize,
                itemStyle: {
                    normal: {
                        color: item.itemStyle.normal.color,
                        borderColor: item.itemStyle.normal.borderColor
                    }
                },
                data: item.data.map(function(value) {
                    return value
                })
            }
        })
    })
}