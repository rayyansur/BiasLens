import type { AnalysisResult, AnalyzeRequest } from "@/types/analysis";

const BASE_URL = process.env.NEXT_PUBLIC_API_URL ?? "http://localhost:8000";

async function request<T>(path: string, init?: RequestInit): Promise<T> {
  const res = await fetch(`${BASE_URL}${path}`, {
    ...init,
    headers: {
      "Content-Type": "application/json",
      ...(init?.headers ?? {}),
    },
  });
  if (!res.ok) {
    const detail = await res.text();
    throw new Error(`API ${res.status}: ${detail}`);
  }
  return res.json() as Promise<T>;
}

function authHeaders(token: string): HeadersInit {
  return { Authorization: `Bearer ${token}` };
}

export const api = {
  analyze(token: string, body: AnalyzeRequest): Promise<AnalysisResult> {
    return request("/analyze", {
      method: "POST",
      headers: authHeaders(token),
      body: JSON.stringify(body),
    });
  },

  getAnalysis(token: string, id: number): Promise<AnalysisResult> {
    return request(`/analysis/${id}`, { headers: authHeaders(token) });
  },

  getHistory(token: string, page = 1, pageSize = 20): Promise<AnalysisResult[]> {
    return request(`/history?page=${page}&page_size=${pageSize}`, {
      headers: authHeaders(token),
    });
  },
};
