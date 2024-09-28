<template>
  <v-container>
    <v-row justify="center">
      <v-col cols="12" md="4" class="d-flex justify-center">
        <v-img src="/dp.png" alt="App Logo" max-width="100" max-height="100"></v-img>
      </v-col>
    </v-row>

   
    <v-sheet height="400px" class="d-flex align-center justify-center hero-background" elevation="0">
      <div class="text-center">
        <h1 class="display-2 font-weight-bold mb-4">🤖 AI Data Predictor</h1>
        <p class="subtitle-1 mb-4">
          Upload your CSV, choose your target column, and get predictions powered by advanced AI models.
        </p>

        <v-btn color="primary" large @click="scrollToUpload"> 🤗 Get Started </v-btn>
      </div>
    </v-sheet>

 
    <v-card class="form-card mt-5" elevation="2" id="upload-section">
      <v-card-title>📂 Upload Your Data</v-card-title>
      <v-card-text>
        <v-form ref="form" @submit.prevent="submitCSV">
          <v-file-input v-model="csvFile" label="Upload CSV" accept=".csv" required outlined></v-file-input>
          <v-btn color="primary" type="submit" :disabled="!csvFile">Submit</v-btn>
        </v-form>
      </v-card-text>
    </v-card>


    <v-card v-if="columns.length > 0" class="form-card mt-5" elevation="2">
      <v-card-title>🔍 Select Your Target Column</v-card-title>
      <v-card-text>
        <v-select v-model="selectedTarget" :items="columns" label="Target Column" required outlined></v-select>

    
        <v-row>
          <v-col v-for="column in columns" :key="column" cols="12" md="6">
            <v-text-field
              v-if="column !== selectedTarget"
              v-model="inputs[column]"
              :label="`Enter value for ${column}`"
              outlined
            ></v-text-field>
          </v-col>
        </v-row>

        <v-btn color="primary" @click="submitPrediction">🤗 Get Predictions</v-btn>
      </v-card-text>
    </v-card>

   
    <v-skeleton-loader v-if="loading" :loading="loading" type="card" height="100px" class="mt-5 md-10"></v-skeleton-loader>

   
    <v-card v-if="!loading && predictions.length > 0" class="result-card mt-5" elevation="2">
      <v-card-title>Prediction Results</v-card-title>
      <v-card-text>
        <div v-if="predictions[0].prediction_score">
          <strong>Prediction:</strong> {{ predictions[0].prediction_label }} <br />
          <strong>Prediction Score:</strong> {{ predictions[0].prediction_score }}
        </div>
        <div v-else>
          <strong>Prediction:</strong> {{ predictions[0].prediction_label }}
        </div>
      </v-card-text>
    </v-card>

    <v-footer class="ma-10 pa-6 hero-background">
      <v-container>
        <v-row justify="center">
          <p>
            Made with <span style="color: red;"> ❤ </span> by
            <a href="https://www.linkedin.com/in/pablo-sierra-fernandez" target="_blank" style="color: black;">
              Pablo Sierra
            </a>
          </p>
        </v-row>
      </v-container>
    </v-footer>
  </v-container>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

// Refs for state management
const csvFile = ref(null);
const columns = ref([]);
const selectedTarget = ref('');
const inputs = ref({});
const predictions = ref([]);
const loading = ref(false);

// Scroll to upload section
const scrollToUpload = () => {
  const element = document.getElementById('upload-section');
  element.scrollIntoView({ behavior: 'smooth' });
};

// Submit CSV to get columns
const submitCSV = async () => {
  const formData = new FormData();
  formData.append('file', csvFile.value);

  try {
    const response = await axios.post('http://127.0.0.1:8000/upload-csv/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });

    if (response && response.data) {
      columns.value = response.data.columns;
      inputs.value = {}; // Reset inputs
    } else {
      console.error('No data in response:', response);
    }
  } catch (error) {
    console.error('Error uploading CSV:', error);
  }
};

// Submit for prediction
const submitPrediction = async () => {
  const formData = new FormData();
  formData.append('file', csvFile.value);
  formData.append('target_column', selectedTarget.value);

  // Serialize input columns data
  const columnsData = JSON.stringify(inputs.value);
  formData.append('columns', columnsData);

  loading.value = true;

  try {
    const { data } = await axios.post('http://127.0.0.1:8000/predict/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
    predictions.value = data;
  } catch (error) {
    console.error('Error fetching predictions:', error);
  } finally {
    loading.value = false;
  }
};
</script>

<style>
.hero-background {
  background: linear-gradient(135deg, #fffff3, #c5fff69f, #ffe4fa);
}

.text-center h1 {
  color: #212121;
}

.text-center p {
  color: #757575;
}

.text-center {
  margin-top: -40px;
}

.mt-5 {
  margin-top: 40px;
}
</style>
