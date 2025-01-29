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
import {
  Select,
  SelectContent,
  SelectItem,
  SelectTrigger,
  SelectValue,
} from '@/components/ui/select';
import { formatValue, getValue } from '@/lib/utils';
import { DashboardNav } from '@/components/nav';
import Link from 'next/link';
import { Spinner } from '@/components/ui/spinner';

const metrics = [
  {
    id: 'gdp',
    name: 'GDP',
    valueKey: 'economy.economic_metrics.gross_domestic_product_gdp',
    order: 'desc',
  },
  {
    id: 'gdp_per_capita',
    name: 'GDP per Capita',
    derived: true,
    getValue: (state) => {
      const gdpMetric = getValue(
        state,
        'economy.economic_metrics.gross_domestic_product_gdp'
      );
      const populationMetric = getValue(
        state,
        'people.people_metrics.total_population'
      );

      if (
        !gdpMetric?.value ||
        !populationMetric?.value ||
        populationMetric.value < 1000000
      ) {
        return {
          value: 0,
          unit: 'USD',
          raw: '$0',
          key: 'GDP per Capita',
        };
      }

      const value = gdpMetric.value / populationMetric.value;
      return {
        value,
        unit: 'USD',
        raw: `$${new Intl.NumberFormat('en-US').format(Math.round(value))}`,
        key: 'GDP per Capita',
      };
    },
    order: 'desc',
  },
  {
    id: 'population',
    name: 'Population',
    valueKey: 'people.people_metrics.total_population',
    order: 'desc',
  },
  {
    id: 'approval',
    name: 'Approval Rating',
    valueKey:
      'government.government_metrics.overall_head_of_stategovernment_approval_rating',
    order: 'desc',
  },
  {
    id: 'hdi',
    name: 'Human Development Index',
    valueKey: 'people.people_metrics.human_development_index_hdi',
    order: 'desc',
  },
  {
    id: 'happiness',
    name: 'World Happiness Score',
    valueKey: 'people.people_metrics.gallup_world_happiness_score',
    order: 'desc',
  },
  {
    id: 'social_mobility',
    name: 'Social Mobility Index',
    valueKey: 'people.people_metrics.social_mobility_index',
    order: 'desc',
  },
  {
    id: 'corruption',
    name: 'Corruption Index',
    valueKey: 'government.government_metrics.corruption_perception_index_cpi',
    order: 'asc',
  },
  {
    id: 'life_expectancy',
    name: 'Life Expectancy',
    valueKey: 'health.life_expectancy.average_life_expectancy_at_birth',
    order: 'desc',
  },
  {
    id: 'unemployment',
    name: 'Unemployment Rate',
    valueKey: 'economy.economic_metrics.unemployment_rate',
    order: 'asc',
  },
  {
    id: 'air_quality',
    name: 'Air Quality Index',
    valueKey:
      'geography_and_environment.environmental_metrics.air_quality_index',
    order: 'asc',
  },
  {
    id: 'poverty_rate',
    name: 'Poverty Rate',
    valueKey: 'economy.economic_metrics.poverty_rate',
    order: 'asc',
  },
  {
    id: 'gini',
    name: 'Gini Coefficient',
    valueKey: 'economy.economic_metrics.gini_coefficient',
    order: 'asc',
  },
];

export default function LeaderboardPage() {
  const [states, setStates] = useState([]);
  const [selectedMetric, setSelectedMetric] = useState(metrics[0].id);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    async function fetchData() {
      try {
        const latestSnapshots = await api._get('/api/states/latest');
        setStates(latestSnapshots);
      } finally {
        setIsLoading(false);
      }
    }
    fetchData();
  }, []);

  const sortedStates = [...states].sort((a, b) => {
    const metric = metrics.find((m) => m.id === selectedMetric);
    let valueA, valueB;

    if (metric.derived) {
      valueA = metric.getValue(a.latest_snapshot.json_state)?.value || 0;
      valueB = metric.getValue(b.latest_snapshot.json_state)?.value || 0;
    } else {
      valueA =
        getValue(a.latest_snapshot.json_state, metric.valueKey)?.value || 0;
      valueB =
        getValue(b.latest_snapshot.json_state, metric.valueKey)?.value || 0;
    }

    const order = metric.order === 'desc' ? 1 : -1;
    return (valueB - valueA) * order;
  });

  return (
    <div className="flex min-h-screen flex-col">
      <DashboardNav />
      <main className="flex-1 px-4">
        <div className="container py-8 space-y-8">
          <div className="flex items-center justify-between">
            <h1 className="text-3xl font-bold">Leaderboard</h1>
          </div>

          <div className="w-[200px] mb-4">
            <Select value={selectedMetric} onValueChange={setSelectedMetric}>
              <SelectTrigger>
                <SelectValue placeholder="Select metric" />
              </SelectTrigger>
              <SelectContent>
                {metrics.map((metric) => (
                  <SelectItem key={metric.id} value={metric.id}>
                    {metric.name}
                  </SelectItem>
                ))}
              </SelectContent>
            </Select>
          </div>

          <div className="rounded-md border p-4">
            {isLoading ? (
              <div className="flex justify-center items-center py-8">
                <Spinner className="w-8 h-8" />
              </div>
            ) : (
              <>
                {states.length > 0 && states[0].cache_updated_at && (
                  <div className="text-sm text-muted-foreground mb-4">
                    Last updated:{' '}
                    {new Date(states[0].cache_updated_at).toLocaleString(
                      undefined,
                      {
                        dateStyle: 'medium',
                        timeStyle: 'medium',
                      }
                    )}
                  </div>
                )}
                <Table>
                  <TableHeader>
                    <TableRow>
                      <TableHead className="w-12">Rank</TableHead>
                      <TableHead className="w-8"></TableHead>
                      <TableHead>Name</TableHead>
                      <TableHead>Year</TableHead>
                      <TableHead className="text-right">
                        {metrics.find((m) => m.id === selectedMetric)?.name}
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
                            href={`/state/${state.id}?showInfo=true`}
                            className="hover:underline"
                          >
                            {state.name}
                          </Link>
                        </TableCell>
                        <TableCell>
                          {new Date(state.latest_snapshot.date).getFullYear()}
                        </TableCell>
                        <TableCell className="text-right">
                          {(() => {
                            const metric = metrics.find(
                              (m) => m.id === selectedMetric
                            );
                            if (metric.derived) {
                              const result = metric.getValue(
                                state.latest_snapshot.json_state
                              );
                              return result?.raw || '$0';
                            }
                            return formatValue(
                              state.latest_snapshot.json_state,
                              metric.valueKey
                            );
                          })()}
                        </TableCell>
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}
