'use client';

import { useState, useEffect, Suspense } from 'react';
import { DashboardNav } from '@/components/nav';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import OverviewPage from '@/components/dashboard/overview';
import PeoplePage from '@/components/dashboard/people';
import EducationPage from '@/components/dashboard/education';
import HealthPage from '@/components/dashboard/health';
import CrimePage from '@/components/dashboard/crime';
import GovernmentPage from '@/components/dashboard/government';
import EconomyPage from '@/components/dashboard/economy';
import MilitaryPage from '@/components/dashboard/military';
import CulturePage from '@/components/dashboard/culture';
import GeographyPage from '@/components/dashboard/geography';
import InfrastructurePage from '@/components/dashboard/infrastructure';
import InternationalRelationsPage from '@/components/dashboard/international-relations';
import MediaPage from '@/components/dashboard/media';
import { api } from '@/lib/api';
import { Badge } from '@/components/ui/badge';
import { PlayDialog } from '@/components/dashboard/play-dialog';
import { InfoDialog } from '@/components/info-dialog';
import { ReportDialog } from '@/components/dashboard/report-dialog';
import { cn } from '@/lib/utils';
import { FlagSVG } from '@/components/flag-svg';
import { useUser } from '@/context/user-context';
import { useSearchParams } from 'next/navigation';

function StatePageContent({ stateId }) {
  const searchParams = useSearchParams();
  const { refreshStates, user } = useUser();
  const [state, setState] = useState(null);
  const [snapshots, setSnapshots] = useState([]);
  const [turnLoading, setTurnLoading] = useState(false);
  const [loadingMessage, setLoadingMessage] = useState('');
  const [reportOpen, setReportOpen] = useState(false);
  const [helpOpen, setHelpOpen] = useState(
    searchParams.get('showInfo') === 'true'
  );
  const [latestReport, setLatestReport] = useState('');
  const latestSnapshot = snapshots[0];
  const isOwner = state?.user_id === user?.id;
  console.log('latest', snapshots, latestSnapshot);

  useEffect(() => {
    api.getStateSnapshots(stateId).then((snaps) => {
      setSnapshots(snaps.map((snap) => snap.json_state));
    });
  }, [stateId]);

  useEffect(() => {
    api.getState(stateId).then((state) => {
      setState(state);
    });
  }, [stateId]);

  const handlePlay = (policy) => {
    setTurnLoading(true);
    setLoadingMessage('Starting simulation...');
    api.createStateSnapshot(stateId, policy, (event) => {
      switch (event.type) {
        case 'status':
          setLoadingMessage(event.message);
          break;
        case 'state_snapshot_complete':
          setSnapshots((prevSnapshots) => [
            event.state_snapshot.json_state,
            ...prevSnapshots,
          ]);
          refreshStates();
          // hard refresh previous snapshots in case they changed
          setTimeout(() => {
            api.getStateSnapshots(stateId).then((snaps) => {
              setSnapshots(snaps.map((snap) => snap.json_state));
            });
          }, 1000);
          setTurnLoading(false);
          setLoadingMessage('');
          if (event.state_snapshot.markdown_delta_report) {
            setLatestReport(event.state_snapshot.markdown_delta_report);
            setReportOpen(true);
          }
          break;
      }
    });
  };

  return (
    <div className="flex flex-col min-h-screen">
      <DashboardNav stateId={stateId} />
      <div className="flex-1 space-y-4 p-8 pt-6">
        <div className="flex flex-col space-y-4 sm:flex-row sm:items-center sm:justify-between sm:space-y-0">
          <div className="flex flex-col gap-2 sm:flex-row sm:items-center">
            <div className="flex items-center gap-3">
              <FlagSVG
                svgString={state?.flag_svg}
                size="2rem"
                allowExpand={true}
              />
              <h2
                className={cn(
                  'text-3xl font-bold tracking-tight',
                  turnLoading && 'animate-pulse'
                )}
              >
                {
                  latestSnapshot?.government.government_metadata
                    .country_official_name.value
                }
              </h2>
            </div>
            <Badge variant="secondary">
              {
                latestSnapshot?.government.government_metadata.government_type
                  .value
              }
            </Badge>
          </div>
          {isOwner && (
            <div className="flex items-center space-x-2">
              <PlayDialog
                stateId={stateId}
                date={latestSnapshot?.date}
                events={latestSnapshot?.events}
                eventsPolicy={latestSnapshot?.events_policy}
                onPlay={handlePlay}
                turnLoading={turnLoading}
                loadingMessage={loadingMessage}
                key={latestSnapshot?.date}
              />
              <InfoDialog
                title="How to Play"
                state={state}
                open={helpOpen}
                onOpenChange={setHelpOpen}
                includeInstructions={true}
              />
            </div>
          )}
          {!isOwner && (
            <InfoDialog
              title={state?.name}
              state={state}
              open={helpOpen}
              onOpenChange={setHelpOpen}
              includeInstructions={false}
            />
          )}
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
              <TabsTrigger value="education">Education</TabsTrigger>
              <TabsTrigger value="health">Health</TabsTrigger>
              <TabsTrigger value="crime">Crime</TabsTrigger>
              <TabsTrigger value="media">Media</TabsTrigger>
              <TabsTrigger value="economy">Economy</TabsTrigger>
              <TabsTrigger value="government">Government</TabsTrigger>
              <TabsTrigger value="military">Military</TabsTrigger>
              <TabsTrigger value="culture">Culture</TabsTrigger>
              <TabsTrigger value="geography">Geography</TabsTrigger>
              <TabsTrigger value="infrastructure">Infrastructure</TabsTrigger>
              <TabsTrigger value="international-relations">
                International
              </TabsTrigger>
            </TabsList>
          </div>

          <TabsContent value="overview" className="space-y-4">
            <OverviewPage snapshots={snapshots} />
          </TabsContent>

          <TabsContent value="people" className="space-y-4">
            <PeoplePage snapshots={snapshots} />
          </TabsContent>

          <TabsContent value="education" className="space-y-4">
            <EducationPage snapshots={snapshots} />
          </TabsContent>

          <TabsContent value="health" className="space-y-4">
            <HealthPage snapshots={snapshots} />
          </TabsContent>

          <TabsContent value="crime" className="space-y-4">
            <CrimePage snapshots={snapshots} />
          </TabsContent>

          <TabsContent value="media" className="space-y-4">
            <MediaPage snapshots={snapshots} />
          </TabsContent>

          <TabsContent value="economy" className="space-y-4">
            <EconomyPage snapshots={snapshots} />
          </TabsContent>

          <TabsContent value="government" className="space-y-4">
            <GovernmentPage snapshots={snapshots} />
          </TabsContent>

          <TabsContent value="military" className="space-y-4">
            <MilitaryPage snapshots={snapshots} />
          </TabsContent>

          <TabsContent value="culture" className="space-y-4">
            <CulturePage snapshots={snapshots} />
          </TabsContent>

          <TabsContent value="geography" className="space-y-4">
            <GeographyPage snapshots={snapshots} />
          </TabsContent>

          <TabsContent value="infrastructure" className="space-y-4">
            <InfrastructurePage snapshots={snapshots} />
          </TabsContent>

          <TabsContent value="international-relations" className="space-y-4">
            <InternationalRelationsPage snapshots={snapshots} />
          </TabsContent>
        </Tabs>
      </div>
    </div>
  );
}

export default function StatePage({ stateId }) {
  return (
    <Suspense fallback={<div>Loading...</div>}>
      <StatePageContent stateId={stateId} />
    </Suspense>
  );
}
