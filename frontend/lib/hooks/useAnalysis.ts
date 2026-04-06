"use client";

import { useState } from "react";
import { api } from "@/lib/api";
import type { AnalysisResult } from "@/types/analysis";

export function useAnalysis(token: string) {
  const [result, setResult] = useState<AnalysisResult | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function analyze(text: string) {
    setLoading(true);
    setError(null);
    try {
      const data = await api.analyze(token, { text });
      setResult(data);
    } catch (e) {
      setError(e instanceof Error ? e.message : "Unknown error");
    } finally {
      setLoading(false);
    }
  }

  return { result, loading, error, analyze };
}
