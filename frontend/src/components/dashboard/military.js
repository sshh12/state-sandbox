import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { ScrollArea } from '@/components/ui/scroll-area';
import MetricCard from './metric-card';
import ChallengesCard from './challenges-card';
import { Users, Plane, Anchor, Truck, Laptop, UserCog } from 'lucide-react';

export default function MilitaryPage({ snapshots }) {
  const latestSnapshot = snapshots[0];
  if (!latestSnapshot) return null;

  const { military_system, military_assets, top_defense_challenges } =
    latestSnapshot.defense;

  // Group assets by category
  const airAssets = {
    'Advanced Combat Aircraft':
      military_assets.advanced_combat_aircraft_thth_gen,
    'Basic Combat Aircraft': military_assets.basic_combat_aircraft_rdnd_gen,
    'Transport/Support Aircraft': military_assets.transportsupport_aircraft,
    'Combat Helicopters': military_assets.combat_helicopters,
    'Support Helicopters': military_assets.support_helicopters,
    'Unmanned Systems': military_assets.unmanned_aerial_systems,
  };

  const navalAssets = {
    'Major Combat Ships': military_assets.major_combat_ships,
    'Minor Combat Ships': military_assets.minor_combat_ships,
    Submarines: military_assets.submarines,
    'Support Vessels': military_assets.support_vessels,
  };

  const groundAssets = {
    'Modern Battle Tanks': military_assets.modern_main_battle_tanks,
    'Legacy Tanks': military_assets.legacy_tanks,
    'Armored Vehicles': military_assets.armored_combat_vehicles,
    'Artillery Systems': military_assets.artillery_systems,
    'Air Defense Systems': military_assets.air_defense_systems,
  };

  const specialAssets = {
    'Satellite Systems': military_assets.satellite_systems,
    'Cyber/Electronic Units': military_assets.cyberelectronic_warfare_units,
    'Special Forces': military_assets.special_forces_units,
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
        {/* Air Assets */}
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-base font-medium">Air Assets</CardTitle>
            <Plane className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <ScrollArea className="h-[200px]">
              <div className="space-y-2">
                {Object.entries(airAssets).map(([name, asset]) => (
                  <div key={name} className="flex justify-between items-center">
                    <span className="text-sm text-muted-foreground">
                      {name}
                    </span>
                    <span className="font-medium">{asset.raw}</span>
                  </div>
                ))}
              </div>
            </ScrollArea>
          </CardContent>
        </Card>

        {/* Naval Assets */}
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-base font-medium">
              Naval Assets
            </CardTitle>
            <Anchor className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <ScrollArea className="h-[200px]">
              <div className="space-y-2">
                {Object.entries(navalAssets).map(([name, asset]) => (
                  <div key={name} className="flex justify-between items-center">
                    <span className="text-sm text-muted-foreground">
                      {name}
                    </span>
                    <span className="font-medium">{asset.raw}</span>
                  </div>
                ))}
              </div>
            </ScrollArea>
          </CardContent>
        </Card>

        {/* Ground Assets */}
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-base font-medium">
              Ground Assets
            </CardTitle>
            <Truck className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <ScrollArea className="h-[200px]">
              <div className="space-y-2">
                {Object.entries(groundAssets).map(([name, asset]) => (
                  <div key={name} className="flex justify-between items-center">
                    <span className="text-sm text-muted-foreground">
                      {name}
                    </span>
                    <span className="font-medium">{asset.raw}</span>
                  </div>
                ))}
              </div>
            </ScrollArea>
          </CardContent>
        </Card>

        {/* Special Assets */}
        <Card>
          <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-2">
            <CardTitle className="text-base font-medium">
              Special Assets
            </CardTitle>
            <Laptop className="h-4 w-4 text-muted-foreground" />
          </CardHeader>
          <CardContent>
            <ScrollArea className="h-[200px]">
              <div className="space-y-2">
                {Object.entries(specialAssets).map(([name, asset]) => (
                  <div key={name} className="flex justify-between items-center">
                    <span className="text-sm text-muted-foreground">
                      {name}
                    </span>
                    <span className="font-medium">{asset.raw}</span>
                  </div>
                ))}
              </div>
            </ScrollArea>
          </CardContent>
        </Card>
      </div>
    </div>
  );
}
