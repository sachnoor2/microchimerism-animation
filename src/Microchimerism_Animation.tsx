import { AbsoluteFill, Series, interpolate, useCurrentFrame, useVideoConfig } from 'remotion';
import { Title, Body, Background, PhysicsModel } from './components/HidictStudio';

export const MicrochimerismShort = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  return (
    <AbsoluteFill style={{ backgroundColor: '#0E1117' }}>
      <Series>
        {/* 0-3s: Claim Slam */}
        <Series.Sequence durationInFrames={180}>
          <Title text="YOU ARE INSIDE HER HEART" color="#FDCB6E" />
        </Series.Sequence>
        
        {/* 3-25s: Mechanism */}
        <Series.Sequence durationInFrames={1320}>
          <PhysicsModel type="fetal_cell_migration" />
          <Body text="Fetal cells repair Mother's tissue" color="#00CEC9" />
        </Series.Sequence>
        
        {/* 25-45s: Twist & CTA */}
        <Series.Sequence durationInFrames={1200}>
          <Title text="A PERMANENT BOND" color="#E17055" />
          <Body text="Did you know you healed her?" color="#FDCB6E" />
        </Series.Sequence>
      </Series>
    </AbsoluteFill>
  );
};