interface Props {
  driftScore: number; // [0, 1]
}

function driftColor(score: number): string {
  if (score < 0.33) return "text-green-600";
  if (score < 0.66) return "text-yellow-500";
  return "text-red-600";
}

export function NarrativeDriftChart({ driftScore }: Props) {
  return (
    <div className="flex flex-col items-center gap-2">
      <p className="text-sm text-gray-500">Narrative Drift Score</p>
      <p className={`text-4xl font-bold ${driftColor(driftScore)}`}>
        {driftScore.toFixed(2)}
      </p>
      <div className="w-full h-3 rounded-full bg-gradient-to-r from-green-400 via-yellow-400 to-red-500">
        <div
          className="h-3 w-3 rounded-full bg-white border-2 border-gray-600 -mt-0"
          style={{ marginLeft: `calc(${driftScore * 100}% - 6px)` }}
        />
      </div>
    </div>
  );
}
