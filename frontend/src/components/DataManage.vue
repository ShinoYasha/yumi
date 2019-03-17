<template>
    <div>
        <div class="wrapper">
            <div class="title">销售数据</div>
            <div class="desc">
                <strong>数据管理</strong>
            </div>
        </div>
        <div class="bar">搜索条件</div>
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
            <el-button type="primary" @click="queryData">确定</el-button>
        </div>
        <div class="bar">查询结果</div>
        <el-table
            :data="formData.slice((currentPage-1)*10, currentPage * 10)"
            border
            stripe
            style="width: 100%">
            <el-table-column
                prop="0"
                label="品类">
            </el-table-column>
            <el-table-column
                prop="1"
                label="时间">
            </el-table-column>
            <el-table-column
                prop="2"
                label="展现指数">
            </el-table-column>
            <el-table-column
                prop="3"
                label="点击率">
            </el-table-column>
            <el-table-column
                prop="4"
                label="点击转化">
            </el-table-column>
            <el-table-column
                prop="5"
                label="点击指数">
            </el-table-column>
            <el-table-column
                prop="6"
                label="销量">
            </el-table-column>
        </el-table>
        <el-pagination
            background
            layout="prev, pager, next"
            @current-change="changeCurrent"
            :total="formData.length">
        </el-pagination>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            startTime: '2017-12-01',
            endTime: '2019-01-10',
            value: '',
            options: [],
            tableData: [],
            formData: [],
            currentPage: 1,
        }
    },
    mounted() {
        this.getList()
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
            console.log(val)
            this.currentPage = val
        },
        queryData() {
            let startIndex, endIndex
            for(let i in this.tableData[this.value].tableData) {
                if(this.startTime === this.tableData[this.value].tableData[i][1] ) {
                    startIndex = i
                }
                if(this.endTime === this.tableData[this.value].tableData[i][1]) {
                    endIndex = i
                }
            }
            //console.log(startIndex)
            //console.log(endIndex)
            console.log(this.tableData)
            let cur = []
            console.log(this.value)
            for(let j = parseInt(startIndex); j <= parseInt(endIndex); j++) {
                console.log(j)
                cur.push(this.tableData[this.value].tableData[j])
            }
            console.log(cur)
            // console.log(this.formData)
            this.formData = (cur.map(e => {
                return Object.assign({}, e)
            }))
            console.log(this.formData)
        }
    }
};
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
.bar {
    background: #eeeeee;
    height: 60px;
    line-height: 60px;
    text-align: left;
    padding-left: 20px;
    margin-top: 20px;
}
.block {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin-top: 20px;
    text-align: left;
}
.el-pagination {
    margin-top: 20px;
}
</style>

