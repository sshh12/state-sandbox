'use client';

import { useState, useEffect } from 'react';
import { DashboardNav } from '@/components/nav';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import OverviewPage from '@/components/dashboard/overview';
import { api } from '@/lib/api';
import { Badge } from '@/components/ui/badge';
import { PlayDialog } from '@/components/dashboard/play-dialog';
import { HelpDialog } from '@/components/help-dialog';
import { ReportDialog } from '@/components/dashboard/report-dialog';
import { cn } from '@/lib/utils';
import { SafeSVG } from '@/components/ui/safe-svg';

export default function StatePage({ stateId }) {
  const [state, setState] = useState(null);
  const [snapshots, setSnapshots] = useState([]);
  const [turnLoading, setTurnLoading] = useState(false);
  const [reportOpen, setReportOpen] = useState(false);
  const [latestReport, setLatestReport] = useState('');
  console.log('latest', snapshots[0]);

  useEffect(() => {
    api.getStateSnapshots(stateId).then((snaps) => {
      setSnapshots(
        snaps
          .map((snap) => snap.json_state)
          .sort((a, b) => new Date(b.date) - new Date(a.date))
      );
    });
  }, [stateId]);

  useEffect(() => {
    api.getState(stateId).then((state) => {
      setState(state);
    });
  }, [stateId]);

  const handlePlay = (policy) => {
    setTurnLoading(true);
    api.createStateSnapshot(stateId, policy).then((snap) => {
      setSnapshots([...snapshots, snap.json_state]);
      setTurnLoading(false);
      if (snap.markdown_delta_report) {
        setLatestReport(snap.markdown_delta_report);
        setReportOpen(true);
      }
    });
  };

  return (
    <div className="flex flex-col min-h-screen">
      <DashboardNav />

      <div className="flex-1 space-y-4 p-8 pt-6">
        <div className="flex flex-col space-y-4 sm:flex-row sm:items-center sm:justify-between sm:space-y-0">
          <div className="flex flex-col gap-2 sm:flex-row sm:items-center">
            <div className="flex items-center gap-3">
              <SafeSVG svgString={state?.flag_svg} />
              <h2
                className={cn(
                  'text-3xl font-bold tracking-tight',
                  turnLoading && 'animate-pulse'
                )}
              >
                {
                  snapshots[0]?.state_overview.basic_information.country_name
                    .value
                }
              </h2>
            </div>
            <Badge variant="secondary">
              {
                snapshots[0]?.state_overview.basic_information.government_type
                  .value
              }
            </Badge>
          </div>
          <div className="flex items-center space-x-2">
            <PlayDialog
              date={snapshots[0]?.date}
              onPlay={handlePlay}
              turnLoading={turnLoading}
              key={snapshots[0]?.date}
            />
            <HelpDialog />
          </div>
        </div>

        <ReportDialog
          isOpen={reportOpen}
          onOpenChange={setReportOpen}
          report={latestReport}
        />

        <Tabs defaultValue="overview" className="space-y-4">
          <div className="border-b overflow-x-auto">
            <TabsList className="inline-flex min-w-full h-10">
              <TabsTrigger value="overview">Overview</TabsTrigger>
              <TabsTrigger value="people">People</TabsTrigger>
              <TabsTrigger value="health">Health</TabsTrigger>
              <TabsTrigger value="economy">Economy</TabsTrigger>
              <TabsTrigger value="government">Government</TabsTrigger>
              <TabsTrigger value="military">Military</TabsTrigger>
              <TabsTrigger value="culture">Culture</TabsTrigger>
              <TabsTrigger value="geography">Geography</TabsTrigger>
              <TabsTrigger value="infrastructure">Infrastructure</TabsTrigger>
            </TabsList>
          </div>

          <TabsContent value="overview" className="space-y-4">
            <OverviewPage snapshots={snapshots} />
          </TabsContent>
        </Tabs>
      </div>
    </div>
  );
}
