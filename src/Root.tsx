import React from 'react';
import { Composition } from 'remotion';
import { MicrochimerismShort } from './Microchimerism_Animation';

export const RemotionRoot: React.FC = () => {
	return (
		<>
			<Composition
				id="Microchimerism"
				component={MicrochimerismShort}
				durationInFrames={2700}
				fps={60}
				width={1080}
				height={1920}
			/>
		</>
	);
};
