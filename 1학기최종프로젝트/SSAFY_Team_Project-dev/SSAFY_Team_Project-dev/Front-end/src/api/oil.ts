import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000'; // 백엔드 서버 주소

// Oil 데이터 타입 정의
interface OilData {
  id: number;
  basDt: string;
  oilCtg: string;
  wtAvgPrcDisc: number;
}

// Oil 데이터를 가져오는 함수
export function getOilData(): Promise<OilData[]> {
  return axios.get<OilData[]>(`${API_BASE_URL}/market/send_data/oil/`).then(response => response.data);
}