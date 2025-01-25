import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { ScrollArea } from '@/components/ui/scroll-area';
import MetricCard from './metric-card';
import ChallengesCard from './challenges-card';
import { Button } from '@/components/ui/button';
import { LineChart } from 'lucide-react';
import { useState } from 'react';
import { MetricLineChartDialog } from './metric-line-chart-dialog';
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from '@/components/ui/tooltip';
import { Users, UserCog } from 'lucide-react';

function MilitaryAssetCard({ title, assets, snapshots, baseValueKey }) {
  const [showChart, setShowChart] = useState(false);
  const [selectedAsset, setSelectedAsset] = useState(null);

  return (
    <>
      <Card>
        <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
          <CardTitle className="text-base font-medium">{title}</CardTitle>
          <div className="flex items-center gap-2">
            <TooltipProvider>
              <Tooltip>
                <TooltipTrigger asChild>
                  <Button
                    variant="ghost"
                    size="icon"
                    className="h-8 w-8 transition-colors hover:bg-primary hover:text-primary-foreground"
                    onClick={() => {
                      const firstAsset = Object.entries(assets)[0];
                      if (firstAsset) {
                        setSelectedAsset({
                          name: firstAsset[0],
                          valueKey: `defense.military_assets.${firstAsset[1].key}`,
                        });
                        setShowChart(true);
                      }
                    }}
                  >
                    <LineChart className="h-4 w-4" />
                  </Button>
                </TooltipTrigger>
                <TooltipContent>
                  <p>View trend over time</p>
                </TooltipContent>
              </Tooltip>
            </TooltipProvider>
          </div>
        </CardHeader>
        <CardContent>
          <ScrollArea className="h-[300px]">
            <div className="space-y-2">
              {Object.entries(assets).map(([name, asset]) => (
                <div
                  key={name}
                  className="flex justify-between items-center group cursor-pointer hover:bg-muted/50 rounded-md p-1 transition-colors"
                  onClick={() => {
                    setSelectedAsset({
                      name,
                      valueKey: `defense.military_assets.${asset.key}`,
                    });
                    setShowChart(true);
                  }}
                >
                  <span className="text-sm text-muted-foreground">{name}</span>
                  <div className="flex items-center gap-2">
                    <span className="font-medium">{asset.raw}</span>
                    <LineChart className="h-3 w-3 text-muted-foreground opacity-0 group-hover:opacity-100 transition-opacity" />
                  </div>
                </div>
              ))}
            </div>
          </ScrollArea>
        </CardContent>
      </Card>
      {snapshots && selectedAsset && (
        <MetricLineChartDialog
          isOpen={showChart}
          onOpenChange={setShowChart}
          title={selectedAsset.name}
          snapshots={snapshots}
          valueKey={selectedAsset.valueKey}
        />
      )}
    </>
  );
}

export default function MilitaryPage({ snapshots }) {
  const latestSnapshot = snapshots[0];
  if (!latestSnapshot) return null;

  const { military_system, military_assets, top_defense_challenges } =
    latestSnapshot.defense;

  // Group assets by category
  const airAssets = {
    'Advanced Combat Aircraft': {
      raw: military_assets.advanced_combat_aircraft_thth_gen.raw,
      key: 'advanced_combat_aircraft_thth_gen',
    },
    'Basic Combat Aircraft': {
      raw: military_assets.basic_combat_aircraft_rdnd_gen.raw,
      key: 'basic_combat_aircraft_rdnd_gen',
    },
    'Transport/Support Aircraft': {
      raw: military_assets.transportsupport_aircraft.raw,
      key: 'transportsupport_aircraft',
    },
    'Combat Helicopters': {
      raw: military_assets.combat_helicopters.raw,
      key: 'combat_helicopters',
    },
    'Support Helicopters': {
      raw: military_assets.support_helicopters.raw,
      key: 'support_helicopters',
    },
    'Unmanned Systems': {
      raw: military_assets.unmanned_aerial_systems.raw,
      key: 'unmanned_aerial_systems',
    },
  };

  const navalAssets = {
    'Major Combat Ships': {
      raw: military_assets.major_combat_ships.raw,
      key: 'major_combat_ships',
    },
    'Minor Combat Ships': {
      raw: military_assets.minor_combat_ships.raw,
      key: 'minor_combat_ships',
    },
    Submarines: {
      raw: military_assets.submarines.raw,
      key: 'submarines',
    },
    'Support Vessels': {
      raw: military_assets.support_vessels.raw,
      key: 'support_vessels',
    },
  };

  const groundAssets = {
    'Modern Battle Tanks': {
      raw: military_assets.modern_main_battle_tanks.raw,
      key: 'modern_main_battle_tanks',
    },
    'Legacy Tanks': {
      raw: military_assets.legacy_tanks.raw,
      key: 'legacy_tanks',
    },
    'Armored Vehicles': {
      raw: military_assets.armored_combat_vehicles.raw,
      key: 'armored_combat_vehicles',
    },
    'Artillery Systems': {
      raw: military_assets.artillery_systems.raw,
      key: 'artillery_systems',
    },
    'Air Defense Systems': {
      raw: military_assets.air_defense_systems.raw,
      key: 'air_defense_systems',
    },
  };

  const specialAssets = {
    'Satellite Systems': {
      raw: military_assets.satellite_systems.raw,
      key: 'satellite_systems',
    },
    'Cyber/Electronic Units': {
      raw: military_assets.cyberelectronic_warfare_units.raw,
      key: 'cyberelectronic_warfare_units',
    },
    'Special Forces': {
      raw: military_assets.special_forces_units.raw,
      key: 'special_forces_units',
    },
  };

  const nuclearAssets = {
    'Strategic Nuclear Warheads': {
      raw: military_assets.strategic_nuclear_warheads.raw,
      key: 'strategic_nuclear_warheads',
    },
    'Tactical Nuclear Warheads': {
      raw: military_assets.tactical_nuclear_warheads.raw,
      key: 'tactical_nuclear_warheads',
    },
    'Nuclear Delivery Systems': {
      raw: military_assets.nuclear_delivery_systems.raw,
      key: 'nuclear_delivery_systems',
    },
    'Ballistic Missile Systems': {
      raw: military_assets.ballistic_missile_systems.raw,
      key: 'ballistic_missile_systems',
    },
  };

  return (
    <div className="space-y-4">
      {/* Top Metrics Grid */}
      <div className="grid gap-4 md:grid-cols-2">
        <MetricCard
          snapshots={snapshots}
          title="Active Personnel"
          valueKey="defense.military_personnel.active_duty_personnel"
          icon={Users}
        />
        <MetricCard
          snapshots={snapshots}
          title="Reserve Personnel"
          valueKey="defense.military_personnel.reserve_personnel"
          icon={UserCog}
        />
      </div>

      {/* Military System Overview and Challenges */}
      <div className="grid gap-4 md:grid-cols-2">
        <Card>
          <CardHeader>
            <CardTitle>Military System</CardTitle>
          </CardHeader>
          <CardContent>
            <p className="text-sm text-muted-foreground">{military_system}</p>
          </CardContent>
        </Card>
        <ChallengesCard
          title="Top Defense Challenges"
          challenges={top_defense_challenges}
        />
      </div>

      {/* Military Assets */}
      <div className="grid gap-4 md:grid-cols-2">
        <MilitaryAssetCard
          title="Air Assets"
          assets={airAssets}
          snapshots={snapshots}
        />
        <MilitaryAssetCard
          title="Naval Assets"
          assets={navalAssets}
          snapshots={snapshots}
        />
        <MilitaryAssetCard
          title="Ground Assets"
          assets={groundAssets}
          snapshots={snapshots}
        />
        <MilitaryAssetCard
          title="Nuclear Assets"
          assets={nuclearAssets}
          snapshots={snapshots}
        />
        <MilitaryAssetCard
          title="Special Assets"
          assets={specialAssets}
          snapshots={snapshots}
        />
      </div>
    </div>
  );
}
