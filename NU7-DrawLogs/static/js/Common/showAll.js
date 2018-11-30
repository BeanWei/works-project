/*
展示所有曲线的公共方法
data: Y轴数据
idStr: HTML中定义的echartdiv的id
title: 图标的标题
tablefunc: 自定义数据视图的函数
Xdata: X轴的数据
*/
function showAll(data, idStr, title, tablefunc, Xdata) {
    var selected = {};
    for (var i in data) {
        selected[data[i].name] = true;
    }
    var myChart = echarts.init(document.getElementById(idStr));
    myChart.clear();
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
            show: false,
        },
        grid: {
            //top: '10%',
            left: '3%',   //图表距边框的距离
            right: '150',
            bottom: '10%',
            containLabel: true
        },
        //工具框，可以选择
        toolbox: {
            x:'center',
            itemGap: 20,
            feature: {
                dataZoom: {},
                dataView: {
                    readOnly: false, 
                    optionToContent: tablefunc,
                },
                restore: {},
                saveAsImage: {},
            }
        },
        //x轴范围滑动
        calculable : true,
        dataZoom : {
            show : true,
            realtime : true,
            start : 0,
            end : 100
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