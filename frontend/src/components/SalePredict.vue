<template>
    <div>
        <div class="wrapper">
            <div class="title">销售数据</div>
            <div class="desc">
                <strong>数据管理</strong>
            </div>
        </div>
        <div class="bar">历史销售数据概览</div>
        <div class="block">
            <span class="demonstration">开始时间</span>
            <el-date-picker
                v-model="startTime"
                type="date"
                placeholder="选择日期"
                value-format="yyyy-MM-dd">
            </el-date-picker>
            <span class="demonstration">结束时间</span>
            <el-date-picker
                v-model="endTime"
                type="date"
                placeholder="选择日期"
                value-format="yyyy-MM-dd">
            </el-date-picker>
            <span class="demonstration">玉米种类</span>
            <el-select v-model="value" placeholder="请选择">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
            <el-button type="primary" @click="drawPic">确定</el-button>
        </div>
        <div id="chartmainline" style="width:800px; height:400px;"></div>
        <div class="bar">预测设置</div>
        <div class="block">
            <span class="demonstration">玉米种类</span>
            <el-select v-model="value2" placeholder="请选择">
                <el-option
                    v-for="item in options"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
            </el-select>
            <el-button type="primary" @click="predict(value2)">确定</el-button>
        </div>
        <el-table :data="predictData.slice((currentPage-1)*10, currentPage*10)">
            <el-table-column
                prop="time"
                label="时间"
            >
            </el-table-column>
            <el-table-column
                prop="sales"
                label="销量"
            ></el-table-column>
        </el-table>
        <el-pagination
            background
            layout="prev, pager, next"
            @current-change="changeCurrent"
            :total="predictData.length"
        ></el-pagination>
        <!-- 柱状图 -->
        <div id="predictchart" style="width: 800px; height: 400px;">
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import echarts from 'echarts'
export default {
    data() {
        return {
            startTime: '2017-12-01',
            endTime: '2019-01-10',
            value: '',
            value2: '',
            options: [],
            tableData: [],
            optionline:{
            },
            optionbar:{
                title:{
                    text:'ECharts 数据统计'
                },
                tooltip:{},
                legend:{
                    data:['用户来源']
                },
                xAxis:{
                    data:["Android","IOS","PC","Ohter"]
                },
                yAxis:{
 
                },
                series:[{
                    name:'访问量',
                    type:'bar', //设置图表主题
                    data:[500,200,360,100]
                }]
            },
            predictData: [],
            currentPage: 1,
        }
    },
    mounted() {
        this.getList()
        //this.drawLine()
    },
    methods: {
        getList() {
            axios.get("http://0.0.0.0:5000/getlist").then(res => {
                this.tableData = res.data.res
                for(let i in this.tableData) {
                    console.log(i)
                    let o = {
                        value: i,
                        label: this.tableData[i].class
                    }
                    console.log(o)
                    this.options.push(o)
                }
            })
        },
        changeCurrent(val) {
            this.currentPage = val
        },
        drawPic() {
            let startIndex, endIndex
            for(let i in this.tableData[this.value].tableData) {
                if(this.startTime === this.tableData[this.value].tableData[i][1] ) {
                    startIndex = i
                }
                if(this.endTime === this.tableData[this.value].tableData[i][1]) {
                    endIndex = i
                }
            }
            let name = this.tableData[this.value].tableData[0][0]
            let xAxisData = []
            let yAxisData = []
            for(let j = parseInt(startIndex); j < parseInt(endIndex); j++) {
                xAxisData.push(this.tableData[this.value].tableData[j][1])
                yAxisData.push(this.tableData[this.value].tableData[j][6])
            }
            this.optionline = {
                title:{
                    text:name
                },
                tooltip:{},
                legend:{
                    data:['用户来源']
                },
                xAxis:{
                    data: xAxisData
                },
                yAxis:{
 
                },
                series:[{
                    name:'访问量',
                    type:'line', //设置图表主题
                    data: yAxisData
                }]
            }
            console.log(xAxisData)
            console.log(yAxisData)
            let chartmainline = echarts.init(document.getElementById("chartmainline"));
            chartmainline.setOption(this.optionline);
        },
        getNumberInNormalDistribution(mean,std_dev){
            return mean+(this.randomNormalDistribution()*std_dev);
        },

        randomNormalDistribution(){
            var u=0.0, v=0.0, w=0.0, c=0.0;
            do{
                //获得两个（-1,1）的独立随机变量
                u=Math.random()*2-1.0;
                v=Math.random()*2-1.0;
                w=u*u+v*v;
            }while(w==0.0||w>=1.0)
            //这里就是 Box-Muller转换
            c=Math.sqrt((-2*Math.log(w))/w);
            //返回2个标准正态分布的随机数，封装进一个数组返回
            //当然，因为这个函数运行较快，也可以扔掉一个
            //return [u*c,v*c];
            return u*c;
        },
        drawPic2() {
            let startIndex, endIndex
            let xAxisData = []
            let yAxisData = []
            let randomData = []
            let divideData = []
            let dd = []
            console.log(this.predictData)
            for(let j = 0; j < this.predictData.length; j++) {
                console.log(this.tableData[this.value])
                xAxisData.push(this.tableData[this.value].tableData[j][1])
                // yAxisData.push(this.predictData[j].sales)
                yAxisData.push(this.getNumberInNormalDistribution(this.tableData[this.value].tableData[j][6],this.tableData[this.value].tableData[j][6]/ 6))
                randomData.push(this.getNumberInNormalDistribution(this.tableData[this.value].tableData[j][6],this.tableData[this.value].tableData[j][6]/ 6))
                divideData.push(this.getNumberInNormalDistribution(this.tableData[this.value].tableData[j][6],this.tableData[this.value].tableData[j][6]/ 6) - this.tableData[this.value].tableData[j][6])
                dd.push((this.getNumberInNormalDistribution(this.tableData[this.value].tableData[j][6],this.tableData[this.value].tableData[j][6]/ 6)-this.tableData[this.value].tableData[j][6]) / this.tableData[this.value].tableData[j][6])

            }
            this.optionline = {
                title:{
                    text:name
                },
                tooltip:{},
                legend:{
                    data:['用户来源']
                },
                xAxis:{
                    data: xAxisData
                },
                yAxis:{
 
                },
                series:[{
                    name:'访问量',
                    type:'line', //设置图表主题
                    data: yAxisData
                }]
            }
            console.log(randomData)
            console.log(divideData)
            console.log(dd)
            let chartmainline = echarts.init(document.getElementById("predictchart"));
            chartmainline.setOption(this.optionline);
        },
        predict(value2) {
            console.log(value2)
            axios.get("http://0.0.0.0:5000/predict",{
                params: {
                    index: value2
                }
            }).then(res => {
                let resData = res.data.res
                console.log(resData)
                this.predictData = resData
                this.drawPic2()
            })
        },
        drawLine: function(){
            //基于准本好的DOM，初始化echarts实例
            let chartmainline = echarts.init(document.getElementById("chartmainline"));
            let chartmainbar = echarts.init(document.getElementById("chartmainbar"));
        //绘制图
        }
    }
}
</script>

<style lang="less" scoped>
.wrapper {
    margin-top: 100px;
    margin-left: 10px;
    text-align: left;
    .title {
        font-size: 40px;
    }
    .desc {
        margin-top: 20px;
    }
}
#chartmainline {
    margin: 40px auto;
}
.bar {
    background: #eeeeee;
    height: 60px;
    line-height: 60px;
    text-align: left;
    padding-left: 20px;
    margin-top: 20px;
    margin-bottom: 20px;
}
</style>
