$.getJSON("../jsonData/Middle_Mic_Fundamental.json", function (data) {
    var selected = {};
    for (var i in data) {
        selected[data[i].name] = true;
    }
    var myChart = echarts.init(document.getElementById("showAllBox"));
    myChart.setOption(option = {
        //标题
        title: {
            text: 'Middle_Mic_Fundamental',
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
                    optionToContent: function(opt) {
                        var axisData = opt.xAxis[0].data;
                        var series = opt.series;
                        var table = '<table class="layui-table" lay-even="" lay-skin="row"><tbody><tr>'
                                    + '<td>SN</td>'
                                    + '<td>100</td>'
                                    + '<td>106</td>'
                                    + '<td>112</td>'
                                    + '<td>118</td>'
                                    + '<td>125</td>'
                                    + '<td>132</td>'
                                    + '<td>140</td>'
                                    + '<td>150</td>'
                                    + '<td>160</td>'
                                    + '<td>170</td>'
                                    + '<td>180</td>'
                                    + '<td>190</td>'
                                    + '<td>200</td>'
                                    + '<td>212</td>'
                                    + '<td>224</td>'
                                    + '<td>236</td>'
                                    + '<td>250</td>'
                                    + '<td>265</td>'
                                    + '<td>280</td>'
                                    + '<td>300</td>'
                                    + '<td>315</td>'
                                    + '<td>335</td>'
                                    + '<td>355</td>'
                                    + '<td>375</td>'
                                    + '<td>400</td>'
                                    + '<td>425</td>'
                                    + '<td>450</td>'
                                    + '<td>475</td>'
                                    + '<td>500</td>'
                                    + '<td>530</td>'
                                    + '<td>560</td>'
                                    + '<td>600</td>'
                                    + '<td>630</td>'
                                    + '<td>670</td>'
                                    + '<td>710</td>'
                                    + '<td>750</td>'
                                    + '<td>800</td>'
                                    + '<td>850</td>'
                                    + '<td>900</td>'
                                    + '<td>950</td>'
                                    + '<td>1000</td>'
                                    + '<td>1060</td>'
                                    + '<td>1120</td>'
                                    + '<td>1180</td>'
                                    + '<td>1250</td>'
                                    + '<td>1320</td>'
                                    + '<td>1400</td>'
                                    + '<td>1500</td>'
                                    + '<td>1600</td>'
                                    + '<td>1700</td>'
                                    + '<td>1800</td>'
                                    + '<td>1900</td>'
                                    + '<td>2000</td>'
                                    + '<td>2120</td>'
                                    + '<td>2240</td>'
                                    + '<td>2360</td>'
                                    + '<td>2500</td>'
                                    + '<td>2650</td>'
                                    + '<td>2800</td>'
                                    + '<td>3000</td>'
                                    + '<td>3150</td>'
                                    + '<td>3350</td>'
                                    + '<td>3550</td>'
                                    + '<td>3750</td>'
                                    + '<td>4000</td>'
                                    + '<td>4250</td>'
                                    + '<td>4500</td>'
                                    + '<td>4750</td>'
                                    + '<td>5000</td>'
                                    + '<td>5300</td>'
                                    + '<td>5600</td>'
                                    + '<td>6000</td>'
                                    + '<td>6300</td>'
                                    + '<td>6700</td>'
                                    + '<td>7100</td>'
                                    + '<td>7500</td>'
                                    + '<td>8000</td>'
                                    + '<td>8500</td>'
                                    + '<td>9000</td>'
                                    + '<td>9500</td>'
                                    + '<td>10000</td>'
                                    + '<td>10600</td>'
                                    + '<td>11200</td>'
                                    + '<td>11800</td>'
                                    + '<td>12500</td>'
                                    + '<td>13200</td>'
                                    + '<td>14000</td>'
                                    + '<td>15000</td>'
                                    + '<td>16000</td>'
                                    + '<td>17000</td>'
                                    + '<td>18000</td>'
                                    + '<td>19000</td>'
                                    + '<td>20000</td>'
                                     + '</tr>';
                        for (var i = 0, l = series.length; i < l; i++) {
                            table += '<tr>'
                                    + '<td>' + series[i].name + '</td>'
                                    + '<td>' + series[i].data[0] + '</td>'
                                    + '<td>' + series[i].data[1] + '</td>'
                                    + '<td>' + series[i].data[2] + '</td>'
                                    + '<td>' + series[i].data[3] + '</td>'
                                    + '<td>' + series[i].data[4] + '</td>'
                                    + '<td>' + series[i].data[5] + '</td>'
                                    + '<td>' + series[i].data[6] + '</td>'
                                    + '<td>' + series[i].data[7] + '</td>'
                                    + '<td>' + series[i].data[8] + '</td>'
                                    + '<td>' + series[i].data[9] + '</td>'
                                    + '<td>' + series[i].data[10] + '</td>'
                                    + '<td>' + series[i].data[11] + '</td>'
                                    + '<td>' + series[i].data[12] + '</td>'
                                    + '<td>' + series[i].data[13] + '</td>'
                                    + '<td>' + series[i].data[14] + '</td>'
                                    + '<td>' + series[i].data[15] + '</td>'
                                    + '<td>' + series[i].data[16] + '</td>'
                                    + '<td>' + series[i].data[17] + '</td>'
                                    + '<td>' + series[i].data[18] + '</td>'
                                    + '<td>' + series[i].data[19] + '</td>'
                                    + '<td>' + series[i].data[20] + '</td>'
                                    + '<td>' + series[i].data[21] + '</td>'
                                    + '<td>' + series[i].data[22] + '</td>'
                                    + '<td>' + series[i].data[23] + '</td>'
                                    + '<td>' + series[i].data[24] + '</td>'
                                    + '<td>' + series[i].data[25] + '</td>'
                                    + '<td>' + series[i].data[26] + '</td>'
                                    + '<td>' + series[i].data[27] + '</td>'
                                    + '<td>' + series[i].data[28] + '</td>'
                                    + '<td>' + series[i].data[29] + '</td>'
                                    + '<td>' + series[i].data[30] + '</td>'
                                    + '<td>' + series[i].data[31] + '</td>'
                                    + '<td>' + series[i].data[32] + '</td>'
                                    + '<td>' + series[i].data[33] + '</td>'
                                    + '<td>' + series[i].data[34] + '</td>'
                                    + '<td>' + series[i].data[35] + '</td>'
                                    + '<td>' + series[i].data[36] + '</td>'
                                    + '<td>' + series[i].data[37] + '</td>'
                                    + '<td>' + series[i].data[38] + '</td>'
                                    + '<td>' + series[i].data[39] + '</td>'
                                    + '<td>' + series[i].data[40] + '</td>'
                                    + '<td>' + series[i].data[41] + '</td>'
                                    + '<td>' + series[i].data[42] + '</td>'
                                    + '<td>' + series[i].data[43] + '</td>'
                                    + '<td>' + series[i].data[44] + '</td>'
                                    + '<td>' + series[i].data[45] + '</td>'
                                    + '<td>' + series[i].data[46] + '</td>'
                                    + '<td>' + series[i].data[47] + '</td>'
                                    + '<td>' + series[i].data[48] + '</td>'
                                    + '<td>' + series[i].data[49] + '</td>'
                                    + '<td>' + series[i].data[50] + '</td>'
                                    + '<td>' + series[i].data[51] + '</td>'
                                    + '<td>' + series[i].data[52] + '</td>'
                                    + '<td>' + series[i].data[53] + '</td>'
                                    + '<td>' + series[i].data[54] + '</td>'
                                    + '<td>' + series[i].data[55] + '</td>'
                                    + '<td>' + series[i].data[56] + '</td>'
                                    + '<td>' + series[i].data[57] + '</td>'
                                    + '<td>' + series[i].data[58] + '</td>'
                                    + '<td>' + series[i].data[59] + '</td>'
                                    + '<td>' + series[i].data[60] + '</td>'
                                    + '<td>' + series[i].data[61] + '</td>'
                                    + '<td>' + series[i].data[62] + '</td>'
                                    + '<td>' + series[i].data[63] + '</td>'
                                    + '<td>' + series[i].data[64] + '</td>'
                                    + '<td>' + series[i].data[65] + '</td>'
                                    + '<td>' + series[i].data[66] + '</td>'
                                    + '<td>' + series[i].data[67] + '</td>'
                                    + '<td>' + series[i].data[68] + '</td>'
                                    + '<td>' + series[i].data[69] + '</td>'
                                    + '<td>' + series[i].data[70] + '</td>'
                                    + '<td>' + series[i].data[71] + '</td>'
                                    + '<td>' + series[i].data[72] + '</td>'
                                    + '<td>' + series[i].data[73] + '</td>'
                                    + '<td>' + series[i].data[74] + '</td>'
                                    + '<td>' + series[i].data[75] + '</td>'
                                    + '<td>' + series[i].data[76] + '</td>'
                                    + '<td>' + series[i].data[77] + '</td>'
                                    + '<td>' + series[i].data[78] + '</td>'
                                    + '<td>' + series[i].data[79] + '</td>'
                                    + '<td>' + series[i].data[80] + '</td>'
                                    + '<td>' + series[i].data[81] + '</td>'
                                    + '<td>' + series[i].data[82] + '</td>'
                                    + '<td>' + series[i].data[83] + '</td>'
                                    + '<td>' + series[i].data[84] + '</td>'
                                    + '<td>' + series[i].data[85] + '</td>'
                                    + '<td>' + series[i].data[86] + '</td>'
                                    + '<td>' + series[i].data[87] + '</td>'
                                    + '<td>' + series[i].data[88] + '</td>'
                                    + '<td>' + series[i].data[89] + '</td>'
                                    + '<td>' + series[i].data[90] + '</td>'
                                    + '<td>' + series[i].data[91] + '</td>'
                                    + '<td>' + series[i].data[92] + '</td>'
                                    + '</tr>';
                        }
                        table += '</tbody></table>';
                        return table;
                    }
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
            data: [100, 106, 112, 118, 125, 132, 140, 150, 160, 170, 180, 190, 200, 212, 224, 236, 250, 265, 280, 300, 315, 335, 355, 375,400, 425, 450, 475, 500, 530, 560, 600, 630, 670, 710, 750, 800, 850, 900, 950, 1000, 1060, 1120, 1180, 1250, 1320, 1400,1500, 1600, 1700, 1800, 1900, 2000, 2120, 2240, 2360, 2500, 2650, 2800, 3000, 3150, 3350, 3550, 3750, 4000, 4250, 4500, 4750,5000, 5300, 5600, 6000, 6300, 6700, 7100, 7500, 8000, 8500, 9000, 9500, 10000, 10600, 11200, 11800, 12500, 13200, 14000, 15000,16000, 17000, 18000, 19000, 20000],
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
})
