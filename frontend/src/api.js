import axios from "axios";

const http = axios.create({ baseURL: "/api" });

export const getVacancies = (params) => http.get("/vacancies/", { params }).then((r) => r.data);
export const getVacancy = (id) => http.get(`/vacancies/${id}`).then((r) => r.data);
export const getProfile = (id) => http.get(`/profiles/${id}`).then((r) => r.data);
export const syncFsp = (id) => http.post(`/profiles/${id}/sync-fsp`).then((r) => r.data);
export const getRecommendations = (id) => http.get(`/matching/${id}`).then((r) => r.data);
