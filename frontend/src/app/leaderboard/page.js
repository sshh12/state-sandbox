'use client';

import { useState, useEffect } from 'react';
import { api } from '@/lib/api';
import { FlagSVG } from '@/components/flag-svg';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table';
import { Tabs, TabsList, TabsTrigger, TabsContent } from '@/components/ui/tabs';
import { formatValue, getValue } from '@/lib/utils';
import { DashboardNav } from '@/components/nav';
import Link from 'next/link';

const metrics = [
  {
    id: 'gdp',
    name: 'GDP',
    valueKey: 'economy.economic_metrics.gross_domestic_product_gdp',
  },
  {
    id: 'population',
    name: 'Population',
    valueKey: 'people.people_metrics.total_population',
  },
  {
    id: 'approval',
    name: 'Approval Rating',
    valueKey:
      'government.government_metrics.overall_head_of_stategovernment_approval_rating',
  },
  {
    id: 'hdi',
    name: 'Human Development Index',
    valueKey: 'people.people_metrics.human_development_index_hdi',
  },
];

export default function LeaderboardPage() {
  const [states, setStates] = useState([]);
  const [selectedMetric, setSelectedMetric] = useState(metrics[0].id);

  useEffect(() => {
    async function fetchData() {
      const latestSnapshots = await api._get('/api/states/latest');
      setStates(latestSnapshots);
    }
    fetchData();
  }, []);

  const selectedMetricKey = metrics.find(
    (m) => m.id === selectedMetric
  )?.valueKey;

  const sortedStates = [...states].sort((a, b) => {
    const valueA =
      getValue(a.latest_snapshot.json_state, selectedMetricKey)?.value || 0;
    const valueB =
      getValue(b.latest_snapshot.json_state, selectedMetricKey)?.value || 0;
    return valueB - valueA;
  });

  return (
    <div className="flex min-h-screen flex-col">
      <DashboardNav />
      <main className="flex-1 px-4">
        <div className="container py-8 space-y-8">
          <div className="flex items-center justify-between">
            <h1 className="text-3xl font-bold">Leaderboard</h1>
          </div>

          <Tabs
            value={selectedMetric}
            onValueChange={setSelectedMetric}
            className="space-y-4"
          >
            <TabsList>
              {metrics.map((metric) => (
                <TabsTrigger key={metric.id} value={metric.id}>
                  {metric.name}
                </TabsTrigger>
              ))}
            </TabsList>

            {metrics.map((metric) => (
              <TabsContent key={metric.id} value={metric.id}>
                <div className="rounded-md border p-4">
                  <Table>
                    <TableHeader>
                      <TableRow>
                        <TableHead className="w-12">Rank</TableHead>
                        <TableHead className="w-8"></TableHead>
                        <TableHead>Name</TableHead>
                        <TableHead className="text-right">
                          {metric.name}
                        </TableHead>
                      </TableRow>
                    </TableHeader>
                    <TableBody>
                      {sortedStates.map((state, index) => (
                        <TableRow key={state.id}>
                          <TableCell className="font-medium">
                            {index + 1}
                          </TableCell>
                          <TableCell>
                            <FlagSVG
                              allowExpand={true}
                              svgString={state.flag_svg}
                              size="1.5rem"
                              className="w-6"
                            />
                          </TableCell>
                          <TableCell>
                            <Link
                              href={`/state/${state.id}`}
                              className="hover:underline"
                            >
                              {state.name}
                            </Link>
                          </TableCell>
                          <TableCell className="text-right">
                            {formatValue(
                              state.latest_snapshot.json_state,
                              metric.valueKey
                            )}
                          </TableCell>
                        </TableRow>
                      ))}
                    </TableBody>
                  </Table>
                </div>
              </TabsContent>
            ))}
          </Tabs>
        </div>
      </main>
    </div>
  );
}
