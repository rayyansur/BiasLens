import type { AnalysisResult } from "@/types/analysis";
import { BiasGauge } from "./BiasGauge";

interface Props {
  analysis: AnalysisResult;
}

export function ArticleCard({ analysis }: Props) {
  return (
    <div className="rounded-lg border border-gray-200 p-4 space-y-3">
      <BiasGauge bias={analysis.bias} score={analysis.bias_score} />
      <p className="text-sm text-gray-500">
        Sentiment: <span className="font-medium capitalize">{analysis.sentiment}</span>{" "}
        ({(analysis.sentiment_score * 100).toFixed(0)}%)
      </p>
      <p className="text-xs text-gray-400">{new Date(analysis.created_at).toLocaleString()}</p>
    </div>
  );
}
