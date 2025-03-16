# Trigger core AI pipeline manually or via cron
import os
print('Running pipeline...')
os.system('python ../backend/ai_core_pipeline.py')
