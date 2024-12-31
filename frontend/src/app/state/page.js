'use client';

import { useState, useEffect } from 'react';
import { DashboardNav } from '@/components/nav';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import OverviewPage from '@/components/dashboard/overview';
import { api } from '@/lib/api';
import { Badge } from '@/components/ui/badge';

export default function StatePage({ stateId }) {
  const [snapshots, setSnapshots] = useState([]);
  const latest = snapshots.sort(
    (a, b) => new Date(b.date) - new Date(a.date)
  )[0];
  console.log('latest', latest);

  useEffect(() => {
    api.getStateSnapshots(stateId).then((snaps) => {
      setSnapshots(snaps.map((snap) => snap.json_state));
    });
  }, [stateId]);

  return (
    <div className="flex flex-col min-h-screen">
      <DashboardNav />

      <div className="flex-1 space-y-4 p-8 pt-6">
        <div className="flex items-center justify-between space-y-2">
          <div className="flex items-center gap-2">
            <h2 className="text-3xl font-bold tracking-tight">
              {latest?.state_overview.basic_information.country_name.value}
            </h2>
            <Badge variant="secondary">
              {latest?.state_overview.basic_information.government_type.value}
            </Badge>
          </div>
          <div className="flex items-center space-x-2">
            <button className="bg-black text-white px-4 py-2 rounded-md">
              Play
            </button>
          </div>
        </div>

        <Tabs defaultValue="overview" className="space-y-4">
          <TabsList>
            <TabsTrigger value="overview">Overview</TabsTrigger>
            <TabsTrigger value="analytics">Analytics</TabsTrigger>
            <TabsTrigger value="reports">Reports</TabsTrigger>
            <TabsTrigger value="notifications">Notifications</TabsTrigger>
          </TabsList>

          <TabsContent value="overview" className="space-y-4">
            <OverviewPage snapshots={snapshots} latest={latest} />
          </TabsContent>
        </Tabs>
      </div>
    </div>
  );
}
