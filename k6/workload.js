import http from 'k6/http';
import { sleep } from 'k6';

export let options = {
  vus: 200000,
  iterations: 100000000
};

export default function () {
  const url = 'https://graph.vshield.pro'; 
  const response = http.get(url);
  console.log("Response status code:", response.status);

  sleep(0.00000001); // オプションの待機時間
}
