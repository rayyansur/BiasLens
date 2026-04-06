"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useAuth } from "@/lib/auth-context";
import { api } from "@/lib/api";
import { useAnalysis } from "@/lib/hooks/useAnalysis";
import { ArticleCard } from "@/components/ArticleCard";
import type { AnalysisResult } from "@/types/analysis";

export default function DashboardPage() {
  const { isAuthenticated, accessToken, logout } = useAuth();
  const router = useRouter();
  const [history, setHistory] = useState<AnalysisResult[]>([]);
  const [text, setText] = useState("");
  const { result, loading, error, analyze } = useAnalysis(accessToken ?? "");

  useEffect(() => {
    if (!isAuthenticated) {
      router.push("/login");
      return;
    }
    api.getHistory(accessToken!).then(setHistory).catch(console.error);
  }, [isAuthenticated, accessToken, router]);

  useEffect(() => {
    if (result) setHistory((prev) => [result, ...prev]);
  }, [result]);

  async function handleAnalyze() {
    if (!text.trim()) return;
    await analyze(text);
    setText("");
  }

  return (
    <main className="min-h-screen bg-gray-50">
      <header className="flex items-center justify-between border-b border-gray-200 bg-white px-8 py-4">
        <h1 className="text-xl font-bold">BiasLens</h1>
        <button
          onClick={logout}
          className="text-sm text-gray-500 hover:text-gray-800"
        >
          Sign out
        </button>
      </header>

      <div className="mx-auto max-w-2xl px-4 py-8 space-y-6">
        <div className="rounded-lg border border-gray-200 bg-white p-6 space-y-3">
          <h2 className="font-semibold">Analyze text</h2>
          <textarea
            value={text}
            onChange={(e) => setText(e.target.value)}
            rows={5}
            placeholder="Paste an article or passage…"
            className="w-full rounded border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
          {error && <p className="text-sm text-red-600">{error}</p>}
          <button
            onClick={handleAnalyze}
            disabled={loading || !text.trim()}
            className="rounded bg-blue-600 px-4 py-2 text-sm font-medium text-white hover:bg-blue-700 disabled:opacity-50"
          >
            {loading ? "Analyzing…" : "Analyze"}
          </button>
        </div>

        {history.length > 0 && (
          <div className="space-y-4">
            <h2 className="font-semibold text-gray-700">Recent analyses</h2>
            {history.map((item) => (
              <a key={item.id} href={`/analysis/${item.id}`}>
                <ArticleCard analysis={item} />
              </a>
            ))}
          </div>
        )}
      </div>
    </main>
  );
}
