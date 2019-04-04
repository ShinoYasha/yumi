<template>
  <div id="app">
    <el-row class="tac">
      <el-col>
        <h5>生产计划管理平台</h5>
        <el-menu
          default-active="2"
          class="el-menu-vertical-demo"
          @open="handleOpen"
          @close="handleClose"
        >
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>销售数据</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="1-1" @click="upload">导入销售数据</el-menu-item>
              <el-menu-item index="1-2" @click="manage">数据管理</el-menu-item>
              <el-menu-item index="1-3" @click="predict">销量预测</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>生产计划</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="2-1" @click="query">数据查询</el-menu-item>
              <el-menu-item index="2-2" @click="plan">制定本年度计划</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
          <el-submenu index="3">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>生产调度</span>
            </template>
            <el-menu-item-group>
              <el-menu-item index="3-1" @click="seed">播种排产</el-menu-item>
              <el-menu-item index="3-2" @click="make">加工排产</el-menu-item>
            </el-menu-item-group>
          </el-submenu>
        </el-menu>
      </el-col>
    </el-row>

    <div class="right">
      <upload-csv v-if="showUploadCsv"></upload-csv>
      <data-manage v-if="showDataManage"></data-manage>
      <sale-predict v-if="showSalePredict"></sale-predict>
      <data-query v-if="showDataQuery"></data-query>
      <produce-plan v-if="showProducePlan"></produce-plan>
      <seed-plan v-if="showSeedPlan"></seed-plan>
      <make-plan v-if="showMakePlan"></make-plan>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import UploadCsv from "./components/UploadCsv.vue";
import DataManage from './components/DataManage.vue'
import SalePredict from './components/SalePredict.vue'
import DataQuery from './components/DataQuery.vue'
import ProducePlan from './components/ProducePlan.vue'
import SeedPlan from './components/SeedPlan.vue'
import MakePlan from './components/MakePlan.vue'
export default {
  name: "App",
  components: { UploadCsv, DataManage, SalePredict, DataQuery, ProducePlan, SeedPlan, MakePlan },
  data() {
    return {
      showUploadCsv: false,
      showDataManage: false,
      showSalePredict: false,
      showDataQuery: false,
      showProducePlan: false,
      showSeedPlan: false,
      showMakePlan: false
    };
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
    upload() {
      this.showUploadCsv = true;
      this.showDataManage = false;
      this.showSalePredict = false;
      this.showDataQuery = false
      this.showProducePlan = false
      this.showSeedPlan = false
      this.showMakePlan = false
    },
    manage() {
        this.showUploadCsv = false;
        this.showDataManage = true
        this.showSalePredict = false
        this.showDataQuery = false
        this.showProducePlan = false
        this.showSeedPlan = false
        this.showMakePlan = false
    },
    predict() {
        this.showUploadCsv = false;
        this.showDataManage = false
        this.showSalePredict = true
        this.showDataQuery = false
        this.showProducePlan = false
        this.showSeedPlan = false
        this.showMakePlan = false
    },
    query() {
        this.showUploadCsv = false
        this.showDataManage = false
        this.showSalePredict = false
        this.showDataQuery = true
        this.showProducePlan = false
        this.showSeedPlan = false
        this.showMakePlan = false
    },
    plan() {
        this.showUploadCsv = false
        this.showDataManage = false
        this.showSalePredict = false
        this.showDataQuery = false
        this.showProducePlan = true
        this.showSeedPlan = false
        this.showMakePlan = false
    },
    seed() {
        this.showUploadCsv = false
        this.showDataManage = false
        this.showSalePredict = false
        this.showDataQuery = false
        this.showProducePlan = false
        this.showSeedPlan = true
        this.showMakePlan = false 
    },
    make() {
        this.showUploadCsv = false
        this.showDataManage = false
        this.showSalePredict = false
        this.showDataQuery = false
        this.showProducePlan = false
        this.showSeedPlan = false
        this.showMakePlan = true
    }
  },
  mounted() {
    axios.get("http://0.0.0.0:5000/clear");
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  display: flex;
}
.tac {
  width: 20%;
}
.right {
  flex-grow: 1;
  padding: 10px;
}
</style>
