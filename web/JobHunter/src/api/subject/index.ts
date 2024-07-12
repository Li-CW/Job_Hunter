import request from '@/utils/request';
enum API {
  SUBJECT_URL = '/subject/',
}

export const subject = () => request.get<any, any>(API.SUBJECT_URL);
