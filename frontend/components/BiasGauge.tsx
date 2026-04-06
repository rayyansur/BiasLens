import type { Bias } from "@/types/analysis";

interface Props {
  bias: Bias;
  score: number;
}

const COLORS: Record<Bias, string> = {
  left: "bg-blue-500",
  center: "bg-gray-400",
  right: "bg-red-500",
};

export function BiasGauge({ bias, score }: Props) {
  return (
    <div className="flex flex-col gap-2">
      <div className="flex justify-between text-sm text-gray-500">
        <span>Left</span>
        <span>Center</span>
        <span>Right</span>
      </div>
      <div className="relative h-4 w-full rounded-full bg-gradient-to-r from-blue-500 via-gray-300 to-red-500">
        <div
          className={`absolute top-0 h-4 w-4 -translate-x-1/2 rounded-full border-2 border-white ${COLORS[bias]}`}
          style={{ left: `${score * 100}%` }}
        />
      </div>
      <p className="text-center text-sm font-medium capitalize">
        {bias} ({(score * 100).toFixed(0)}%)
      </p>
    </div>
  );
}
