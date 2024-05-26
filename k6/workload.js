import http from 'k6/http';
import { check, sleep } from 'k6';

// 負荷テストの設定
const loadTestOptions = {
  vus: 50000, // 負荷テスト時の仮想ユーザーの数
  duration: '60s', // 負荷テスト時の実行時間
};

// 初期状態の設定
export let options = {
  vus: loadTestOptions.vus,
  duration: '10000000000m', // 待機状態の持続時間
  setupTimeout: '10000000000m', // 初期セットアップのタイムアウト
};

export function setup() {
  console.log(`All ${loadTestOptions.vus} VUs initialized and waiting.`);
}

export default function () {
  while (true) {
    let res = http.get('https://your-vercel-app.vercel.app'); // テストするURLを設定
    check(res, {
      'status is 200': (r) => r.status === 200,
    });

    // レスポンスに "start" が含まれているかチェック
    if (res.body.includes('start')) {
      console.log('Start condition met. Initiating load test...');
      break; // ループを抜けて負荷テストを開始
    }

    // 0.5秒待機
    sleep(0.5);
  }

  // 負荷テストの実行
  performLoadTest();
}

function performLoadTest() {
  // 負荷テストのためのリクエストループ
  let endTime = Date.now() + parseDuration(loadTestOptions.duration);
  while (Date.now() < endTime) {
    let res = http.get('https://graph.vshield.pro'); // 負荷テストするURLを設定
    check(res, {
      'status is 200': (r) => r.status === 200,
    });
    sleep(1); // リクエスト間の待機時間
  }
}

function parseDuration(duration) {
  const match = duration.match(/^(\d+)([smhd])$/);
  if (!match) throw new Error(`Invalid duration format: ${duration}`);
  const value = parseInt(match[1], 10);
  const unit = match[2];
  switch (unit) {
    case 's': return value * 1000;
    case 'm': return value * 60 * 1000;
    case 'h': return value * 60 * 60 * 1000;
    case 'd': return value * 24 * 60 * 60 * 1000;
    default: throw new Error(`Unknown time unit: ${unit}`);
  }
}
