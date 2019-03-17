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
            <el-button type="primary" @click="predict">确定</el-button>
        </div>
        <!-- 柱状图 -->
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
            }
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
        predict() {

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
