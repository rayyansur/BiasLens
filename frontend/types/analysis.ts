export type Bias = "left" | "center" | "right";
export type Sentiment = "positive" | "neutral" | "negative";

export interface AnalysisResult {
  id: number;
  bias: Bias;
  bias_score: number;
  sentiment: Sentiment;
  sentiment_score: number;
  created_at: string;
}

export interface AnalyzeRequest {
  text: string;
}
