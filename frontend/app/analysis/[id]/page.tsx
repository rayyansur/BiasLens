import { BiasGauge } from "@/components/BiasGauge";
import { NarrativeDriftChart } from "@/components/NarrativeDriftChart";

interface Props {
  params: { id: string };
}

export default function AnalysisPage({ params }: Props) {
  // Data fetching happens here (server component or useAnalysis hook in a client wrapper)
  return (
    <main className="min-h-screen p-8 space-y-6">
      <h1 className="text-2xl font-bold">Analysis #{params.id}</h1>
      <BiasGauge bias="center" score={0.5} />
      <NarrativeDriftChart driftScore={0} />
    </main>
  );
}
