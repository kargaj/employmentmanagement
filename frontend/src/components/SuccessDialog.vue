<template>
  <v-dialog v-model="localVisible" max-width="500px">
    <v-card>
      <v-card-title class="headline">Success</v-card-title>
      <v-card-text>
        {{ successMessage }}
      </v-card-text>
      <v-card-actions>
        <v-btn color="blue" text @click="closeDialog">Close</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>

<script>
import { defineComponent, ref, watch } from 'vue';

export default defineComponent({
  name: 'SuccessDialog',
  props: {
    visible: {
      type: Boolean,
      required: true
    },
    successMessage: {
      type: String,
      default: "Action completed"
    }
  },
  emits: ['update:visible'],
  setup(props, { emit }) {
    const localVisible = ref(props.visible);

    watch(() => props.visible, (newValue) => {
      localVisible.value = newValue;
    });

    watch(localVisible, (newValue) => {
      emit('update:visible', newValue);
    });

    const closeDialog = () => {
      localVisible.value = false;
    };

    return {
      localVisible,
      closeDialog
    };
  }
});
</script>
