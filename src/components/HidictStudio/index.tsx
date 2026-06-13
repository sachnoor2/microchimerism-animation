import React from 'react';
import { AbsoluteFill, useCurrentFrame, interpolate, spring, useVideoConfig } from 'remotion';

export const Title: React.FC<{ text: string; color: string }> = ({ text, color }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const opacity = interpolate(frame, [0, 20], [0, 1]);
  const scale = spring({ frame, fps, config: { stiffness: 100 } });

  return (
    <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center' }}>
      <h1 style={{
        color,
        fontSize: 100,
        fontFamily: 'Bebas Neue',
        textAlign: 'center',
        opacity,
        transform: `scale(${scale})`
      }}>
        {text}
      </h1>
    </AbsoluteFill>
  );
};

export const Body: React.FC<{ text: string; color: string }> = ({ text, color }) => {
  const frame = useCurrentFrame();
  const opacity = interpolate(frame, [0, 20], [0, 1]);

  return (
    <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center', top: 200 }}>
      <p style={{
        color,
        fontSize: 60,
        fontFamily: 'Bebas Neue',
        textAlign: 'center',
        opacity,
        padding: '0 40px'
      }}>
        {text}
      </p>
    </AbsoluteFill>
  );
};

export const Background: React.FC = () => {
  return <AbsoluteFill style={{ backgroundColor: '#0E1117' }} />;
};

export const PhysicsModel: React.FC<{ type: string }> = ({ type }) => {
  const frame = useCurrentFrame();
  // Simplified visualization for the physics model
  return (
    <AbsoluteFill style={{ justifyContent: 'center', alignItems: 'center' }}>
       <div style={{ color: 'white', fontSize: 40 }}>[Physics Model: {type}]</div>
       {/* In a real scenario, this would be a complex SVG or Canvas animation */}
    </AbsoluteFill>
  );
};
