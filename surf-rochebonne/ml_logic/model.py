



# Optimizer
optimizer = optimizers.Adam(learning_rate=optimizers.schedules.PolynomialDecay(
                            initial_learning_rate=0.001,
                            decay_steps=10000,
                            end_learning_rate=0.0001,
                            power=2.0))

# Neural network model architecture
nn_model = Sequential()
nn_model.add(layers.Input(shape=(X_train_scaled.shape[-1],)))
nn_model.add(layers.Dense(20, activation='relu'))
nn_model.add(layers.Dense(15, activation='relu'))
nn_model.add(layers.Dense(20, activation='relu'))
nn_model.add(layers.Dense(20, activation='relu'))
nn_model.add(layers.Dense(15, activation='relu'))
nn_model.add(layers.Dense(20, activation='relu'))
nn_model.add(layers.Dense(4, activation='softmax'))

# Compiler
nn_model.compile(optimizer=optimizer,loss='categorical_crossentropy',metrics=['accuracy'])

# Fit
history = nn_model.fit(X_train_scaled, y_train_encoded, batch_size=32, epochs=100)
