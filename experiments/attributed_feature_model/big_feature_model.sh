LearnerZ3  \
    --numinstances=-1 \
    --testset=3 \
    --learningiterations=7 \
    --cores=4  \
    --experimentnumsplits 8 \
    --parametersfile big_feature_model.parameters \
    --generatorfile feature_model.cfr \
    --formatter feature_model_formatter.py \
    --heuristics feature_model.heuristics \
    --outputdirectory runs/biggertest/  
